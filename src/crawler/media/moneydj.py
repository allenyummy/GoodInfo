# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class MoneyDJNewsCrawler(BaseMediaCrawler):
    """Web Crawler for MoneyDJ News"""

    MEDIA_CANDIDATES = ["MoneyDJ理財網"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("article", id="MainContent_Contents_mainArticle").text
        logger.debug(f"CONTENT:\n {content}")
        return content
