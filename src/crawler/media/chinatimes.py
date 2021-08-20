# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class ChinatimesNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Chinatimes News"""

    MEDIA_CANDIDATES = ["中時新聞網", "旺得富"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find(
            class_="article-body", itemprop="articleBody"
        ).find_all("p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
