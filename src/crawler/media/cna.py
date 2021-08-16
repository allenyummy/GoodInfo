# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CNANewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for CNA News"""

    MEDIA_CANDIDATES = ["中央社"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="paragraph").text
        logger.debug(f"CONTENT:\n {content}")
        return content
