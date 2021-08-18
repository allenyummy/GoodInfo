# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.config import MEDIA_URL
from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CNYESNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for CNYES News"""

    MEDIA_CANDIDATES = ["鉅亨網", "鉅亨新聞網"]

    def getInfo(self, link: str) -> NewsStruct:
        if MEDIA_URL[self.MEDIA_CANDIDATES[0]] in link:
            link = f"https://news.{'.'.join(link.split('.')[1:])}"
        return super().getInfo(link)

    @staticmethod
    def _get_title(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> str:

        title = soup.find(itemprop="headline").text
        logger.debug(f"TITLE: {title}")
        return title

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find(class_="_2E8y").text
        logger.debug(f"CONTENT:\n {content}\n")
        return content
