# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CMMediaNewsCrawler(BaseMediaCrawler):
    """Web Crawler for CMMedia News"""

    MEDIA_CANDIDATES = ["信傳媒"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("div", class_="article_content").text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_title(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        title = soup.find(property="og:title").get("content")
        logger.debug(f"TITLE: {title}")
        return title

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str], soup: BeautifulSoup
    ) -> Union[List[str], None]:
        keywords = soup.find(itemprop="keywords").get("content").split(",")
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    @staticmethod
    def _get_category(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        category = soup.find(itemtype="articleSection").get("content")
        logger.debug(f"CATEGORY: {category}")
        return category

    @staticmethod
    def _get_datetime(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        datetime = soup.find(itemprop="datePublished").get("content")
        logger.debug(f"DATETIME: {datetime}")
        return datetime
