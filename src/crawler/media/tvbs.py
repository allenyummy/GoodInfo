# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TVBSNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for TVBS News"""

    MEDIA_CANDIDATES = ["TVBS"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", itemprop="articleBody").text

        # Ad changes over time in the same page.
        # It'll cause error during tests.
        # So I have to remove it from content
        ad = soup.find("div", class_="guangxuan").text
        idx = content.find(ad)

        content = content[:idx]
        logger.debug(f"CONTENT:\n {content}")

        return content
