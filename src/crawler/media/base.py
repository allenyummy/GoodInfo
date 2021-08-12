# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Base media crawler for polymorphism

import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union

import requests
from bs4 import BeautifulSoup

from src.config import MEDIA_URL
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class BaseMediaCrawler(ABC):
    """Web Crawler for Media News"""

    MEDIA_CANDIDATES: List[str] = None
    CONTENT_ATTR_PATH: Optional[str] = None

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
    def _get_soup(link: str) -> BeautifulSoup:
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

    @abstractmethod
    def _get_content(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:

        script_info = soup.find("script", type="application/ld+json")
        if not script_info:
            logger.warning("script_info is not found in the soup.")
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
            logger.warning(
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
    def _get_title(script_info: Dict[str, str], soup: BeautifulSoup) -> str:

        title = None
        if script_info and script_info.get("headline"):
            title = script_info.get("headline")
        else:
            title = soup.find("title").text if soup.find("title") else None

        logger.debug(f"TITLE: {title}")
        if not title:
            raise ValueError(
                "TITLE is not found by using BaseMediaCrawler._get_title().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no key of `headline`.\n"
                "3) soup has no `title` tag.\n"
                "Therefore, time to debug!\n"
                "`_get_title` function should not be inheritted but overwritten.\n\n"
            )

        return title

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str], soup: BeautifulSoup
    ) -> Union[List[str], None]:

        keywords = None
        if script_info and script_info.get("keywords"):
            keywords = script_info.get("keywords")
        else:
            keywords = soup.find("news_keywords") or soup.find("keywords")
            keywords = keywords.text if keywords else None

        if keywords and isinstance(keywords, str):
            # Most keywords whose types are string are connected with each other by ",".
            keywords = keywords.split(",")

        logger.debug(f"KEYWORDS: {keywords}")
        if not keywords:
            logger.warning(
                "KEYWORDS are not found by using BaseMediaCrawler._get_keywords().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no key of `keywords`.\n"
                "3) soup has no `news_keywords` or `keywords` tag.\n"
                "Therefore, time to debug!\n"
                "`_get_keywords` function should not be inheritted but overwritten.\n\n"
            )

        return keywords

    @staticmethod
    def _get_category(script_info: Dict[str, str], soup: BeautifulSoup) -> str:

        category = None
        if script_info and script_info.get("articleSection"):
            category = script_info.get("articleSection")

        logger.debug(f"CATEGORY: {category}")
        if not category:
            logger.warning(
                "CATEGORY is not found by using BaseMediaCrawler._get_category().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no key of `articleSection`.\n"
                "3) the article has no category.\n"
                "Therefore, time to debug!\n"
                "`_get_category` function should not be inheritted but overwritten.\n\n"
            )

        return category

    @staticmethod
    def _get_datetime(script_info: Dict[str, str], soup: BeautifulSoup) -> str:

        datetime = None
        if script_info and script_info.get("datePublished"):
            datetime = script_info.get("datePublished")

        logger.debug(f"DATETIME: {datetime}")
        if not datetime:
            logger.warning(
                "DATETIME is not found by using BaseMediaCrawler._get_datetime().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no key of `datePublished`.\n"
                "Therefore, time to debug!\n"
                "`_get_datetime` function should not be inheritted but overwritten.\n\n"
            )

        return datetime

    @staticmethod
    def _get_link(script_info: Dict[str, str]) -> str:

        link = None
        if script_info and script_info.get("mainEntityOfPage"):
            link = script_info.get("mainEntityOfPage")

        logger.debug(f"LINK: {link}")
        if not link:
            logger.warning(
                "LINK is not found by using BaseMediaCrawler._get_link().\n"
                "Possible reasons are as follows:\n"
                "1) script_info is None.\n"
                "2) script_info has no key of `mainEntityOfPage`.\n"
                "Therefore, time to debug!\n"
                "`_get_link` function should not be inheritted but overwritten.\n\n"
            )

        return link
