# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class MirrorNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Mirror News"""

    MEDIA_CANDIDATES = ["鏡週刊"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find_all("p", class_="g-story-paragraph")
        content = "\n".join([s.text for s in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
