# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class NowNewsNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for NowNews News"""

    MEDIA_CANDIDATES = ["今日新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("article", itemprop="articleBody").text
        related = soup.find("ul", class_="related").text
        idx = content.find(related)
        content = content[:idx]
        logger.debug(f"CONTENT:\n {content}")
        return content
