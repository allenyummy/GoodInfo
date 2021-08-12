# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class ETtodayNewsCrawler(BaseMediaCrawler):
    """Web Crawler for ETtoday News"""

    MEDIA_CANDIDATES = ["ETtoday新聞雲", "ETtoday財經雲"]
    CONTENT_ATTR_PATH = ".subject_article .story"

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.select_one(self.CONTENT_ATTR_PATH).text
        logger.debug(f"CONTENT:\n {content}\n")
        return content
