# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CNANewsCrawler(BaseMediaCrawler):
    """Web Crawler for CNA News"""

    MEDIA_CANDIDATES = ["中央社"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("div", class_="paragraph").text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:
        return None

    @staticmethod
    def _get_title(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        title = soup.find(property="og:title").get("content")
        logger.debug(f"TITLE: {title}")
        return title

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str], soup: BeautifulSoup
    ) -> Union[List[str], None]:
        keywords = soup.find("meta", {"name": "keywords"}).get("content").split(",")
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    @staticmethod
    def _get_datetime(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        datetime = soup.find(itemprop="datePublished").get("content")
        logger.debug(f"DATETIME: {datetime}")
        return datetime
