# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Base media crawler for polymorphism

import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup

from src.config import MEDIA_URL
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class BaseMediaNewsCrawler(ABC):
    """Web Crawler for Media News"""

    MEDIA_CANDIDATES: List[str] = None

    def getInfo(self, link: str) -> NewsStruct:

        # Check if NewsCrawler DOES support crawling the given link.
        if not self._get_media(link):
            raise ValueError(
                f"{self.__class__.__name__} only support crawling "
                f"{' and '.join([MEDIA_URL[mc] for mc in self.MEDIA_CANDIDATES])}"
                f", but got {link}."
            )

        # Crawling and Turn to soup
        soup = self._get_soup(link=link)

        # Get a script snippet that is a JSON-LD-based structured data block embedded in HTML
        #    that provides data to User Agents for additional processing.
        # This data can take the form of Metadata
        #    that informs User Agents about the nature of the host documents.
        # By the way, it may be None for some reasons.
        script_info = self._get_script_info(soup=soup)

        return NewsStruct(
            title=self._get_title(script_info, soup),
            keywords=self._get_keywords(script_info, soup),
            category=self._get_category(script_info, soup),
            media=self._get_media(link),
            datetime=self._get_datetime(script_info, soup),
            link=link,
            content=self._get_content(soup),  # last execution for better debug.
        )

    def _get_media(self, link: str) -> Union[str, None]:
        for mc in self.MEDIA_CANDIDATES:
            if MEDIA_URL[mc] in link:
                return mc
        else:
            return None

    @staticmethod
    def _get_soup(
        link: str,
    ) -> BeautifulSoup:
        return BeautifulSoup(
            requests.get(
                link,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                    " AppleWebKit/605.1.15"
                    " (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
                },
            ).text,
            "lxml",
        )

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        script_info = soup.find("script", type="application/ld+json")
        if not script_info:
            logger.debug("script_info is not found in the soup.")
            return script_info

        script_info_str = script_info.string

        try:
            script_info_dict = json.loads(script_info_str, strict=False)
        except Exception as e:
            raise ValueError(
                "script_info is found in the soup, "
                "but failed to transform into dictionary.\n\n"
                "Error message: \n"
                f"{e}\n\n"
                "Possible reasons are as follows:\n"
                "1) there are multiple samples of the pattern (e.g., ftv and ctee).\n"
                "2) expecting property name enclosed in double quotes (e.g., moneyudn).\n"
                "Corresponding solutions are as follows:\n"
                "1) json.loads(soup.find_all()[x].string)\n"
                "2) replace those out-of-format things from script_info_string\n"
                "`_get_script_info` func. should not be inheritted but overwritten.\n\n"
                "Please check script_info_string:\n"
                f"{script_info_str}"
            )

        if not isinstance(script_info_dict, dict):
            script_info_dict = None
            logger.debug(
                "script_info is found in the soup, "
                "but its type is not dictionary.\n\n"
                "Possible reasons are as follows:\n"
                "1) type of script_info is list (e.g., udn).\n"
                "Corresponding solutions are as follows:\n"
                "1) json.loads(soup.find().string)[x]\n"
                "`_get_script_info` func. should not be inheritted but overwritten.\n\n"
                "Please check script_info_string:\n"
                f"{script_info_str}"
            )

        logger.debug(f"SCRIPT_INFO: {script_info_dict}")
        return script_info_dict

    @staticmethod
    def _get_title(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> str:

        title = None
        findfrom_message = ""

        if script_info and script_info.get("headline"):
            title = script_info.get("headline")
            findfrom_message = "script_info has `headline` key."

        elif soup.find("meta", property="og:title"):
            title = soup.find("meta", property="og:title").get("content")
            findfrom_message = "soup has `<meta property='og:title'>`."

        elif soup.find("title"):
            title = soup.find("title").text
            findfrom_message = "soup has `<title>` tag."

        logger.debug(
            f"TITLE: {title}"
            f"{'. Found it because '+ findfrom_message if title else ''}"
        )

        if not title:
            raise ValueError(
                "\n"
                "TITLE is not found by using BaseMediaCrawler._get_title().\n"
                "Possible reasons are as follows:\n"
                "- script_info is None.\n"
                "- script_info has no `headline` key.\n"
                "- soup has no `<meta property='og:title'>`.\n"
                "- soup has no `<title>` tag.\n"
                "Therefore, time to debug!\n"
                "`_get_title` function should not be inheritted but overwritten.\n\n"
            )

        return title

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords = None
        findfrom_message = ""
        possible_attrs = [
            {"name": "news_keywords"},
            {"name": "keywords"},
            {"itemprop": "news_keywords"},
            {"itemprop": "keywords"},
            {"name": "keyword"},
        ]

        if script_info and script_info.get("keywords"):
            keywords = script_info.get("keywords")
            findfrom_message = "script_info has `keywords` key."

        else:
            for attrs in possible_attrs:
                if soup.find("meta", attrs=attrs):
                    keywords = soup.find("meta", attrs=attrs).get("content")
                    key, value = next(iter(attrs.items()))
                    findfrom_message = f"soup has `<meta {key}='{value}'>`."
                    break

        if keywords and isinstance(keywords, str):
            # Most keywords whose types are string are connected with each other by ",".
            if "," in keywords:
                keywords = [k.strip() for k in keywords.split(",")]

            elif "、" in keywords:
                keywords = [k.strip() for k in keywords.split("、")]

            else:
                keywords = [keywords]

        logger.debug(
            f"KEYWORDS: {keywords}"
            f"{'. Found it because '+ findfrom_message if keywords else ''}"
        )

        if not keywords:
            logger.debug(
                "\n"
                "KEYWORDS are not found by using BaseMediaCrawler._get_keywords().\n"
                "Possible reasons are as follows:\n"
                "- script_info is None.\n"
                "- script_info has no `keywords` key.\n"
                + "\n".join(
                    f"- soup has no `<meta {key}={value}>`."
                    for attrs in possible_attrs
                    for key, value in attrs.items()
                )
                + "\n"
                "- this article has no keywords.\n"
                "Therefore, time to debug!\n"
                "`_get_keywords` function should not be inheritted but overwritten.\n\n"
            )

        return keywords

    @staticmethod
    def _get_category(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        category = None
        findfrom_message = ""
        possible_attrs = [
            {"property": "article:section"},
            {"itemprop": "articleSection"},
            {"itemtype": "articleSection"},
            {"name": "section"},
        ]

        if script_info and script_info.get("articleSection"):
            category = script_info.get("articleSection")
            findfrom_message = "script_info has `articleSection` key."

        else:
            for attrs in possible_attrs:
                if soup.find("meta", attrs=attrs):
                    category = soup.find("meta", attrs=attrs).get("content")
                    key, value = next(iter(attrs.items()))
                    findfrom_message = f"soup has `<meta {key}='{value}'>`."
                    break

        logger.debug(
            f"CATEGORY: {category}"
            f"{'. Found it because '+ findfrom_message if category else ''}"
        )

        if not category:
            logger.debug(
                "\n"
                "CATEGORY is not found by using BaseMediaCrawler._get_category().\n"
                "Possible reasons are as follows:\n"
                "- script_info is None.\n"
                "- script_info has no `articleSection` key.\n"
                + "\n".join(
                    f"- soup has no `<meta {key}={value}>`."
                    for attrs in possible_attrs
                    for key, value in attrs.items()
                )
                + "\n"
                "- this article has no category.\n"
                "Therefore, time to debug!\n"
                "`_get_category` function should not be inheritted but overwritten.\n\n"
            )

        return category

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = None
        findfrom_message = ""
        possible_attrs = [
            {"property": "article:published_time"},
            {"itemprop": "datePublished"},
        ]

        if script_info and script_info.get("datePublished"):
            datetime = script_info.get("datePublished")
        else:
            for attrs in possible_attrs:
                if soup.find("meta", attrs=attrs):
                    datetime = soup.find("meta", attrs=attrs).get("content")
                    key, value = next(iter(attrs.items()))
                    findfrom_message = f"soup has `<meta {key}='{value}'>`."
                    break

        logger.debug(f"DATETIME: {datetime}")
        logger.debug(
            f"DATETIME: {datetime}"
            f"{'. Found it because '+ findfrom_message if datetime else ''}"
        )

        if not datetime:
            logger.debug(
                "DATETIME is not found by using BaseMediaCrawler._get_datetime().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no `datePublished` key.\n"
                + "\n".join(
                    f"- soup has no `<meta {key}={value}>`."
                    for attrs in possible_attrs
                    for key, value in attrs.items()
                )
                + "\n"
                "Therefore, time to debug!\n"
                "`_get_datetime` function should not be inheritted but overwritten.\n\n"
            )

        return datetime

    @abstractmethod
    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        raise NotImplementedError
