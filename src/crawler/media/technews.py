# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TechnewsNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Technews News"""

    MEDIA_CANDIDATES = ["科技新報", "財經新報"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="indent").text
        logger.debug(f"CONTENT:\n {content}")
        return content
