# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.config import MEDIA_URL
from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CYNESNewsCrawler(BaseMediaCrawler):
    """Web Crawler for CYNES News"""

    MEDIA_CANDIDATES = ["鉅亨網", "鉅亨新聞網"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        if MEDIA_URL[self.MEDIA_CANDIDATES[0]] in link:
            link = f"https://news.{'.'.join(link.split('.')[1:])}"
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find(class_="_2E8y").text
        logger.debug(f"CONTENT:\n {content}\n")
        return content

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:
        return None

    @staticmethod
    def _get_title(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        title = soup.find(itemprop="headline").text
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
    def _get_datetime(script_info: Dict[str, str], soup: BeautifulSoup) -> str:
        datetime = soup.find(itemprop="datePublished").get("content")
        logger.debug(f"DATETIME: {datetime}")
        return datetime
