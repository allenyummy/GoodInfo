# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class YahooNewsCrawler(BaseMediaCrawler):
    """Web Crawler for Yahoo News"""

    MEDIA_CANDIDATES = ["Yahoo奇摩新聞", "Yahoo奇摩股市"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("div", class_="caas-body").text
        logger.debug(f"CONTENT:\n {content}\n")
        return content
