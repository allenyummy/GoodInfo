# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class LTNNewsCrawler(BaseMediaCrawler):
    """Web Crawler for LTN News"""

    MEDIA_CANDIDATES = ["自由時報電子報", "自由財經"]
    CONTENT_ATTR_PATH = ".whitecon .text"

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.select_one(self.CONTENT_ATTR_PATH).text
        logger.debug(f"CONTENT:\n {content}\n")
        return content
