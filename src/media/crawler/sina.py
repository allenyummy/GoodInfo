# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.media.crawler.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class SINANewsCrawler(BaseMediaCrawler):
    """Web Crawler for SINA News"""

    MEDIA_CANDIDATES = ["新浪新聞"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("div", class_="pcont", itemprop="articleBody").text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_link(script_info: Dict[str, str]) -> str:
        return script_info.get("mainEntityOfPage").get("@id")
