# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class BnextNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Bnext News"""

    MEDIA_CANDIDATES = ["數位時代", "Meet創業小聚"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find("div", class_="htmlview").find_all("p", text=True)
        content = "\n".join([c.string for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
