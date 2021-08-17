# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class KairosNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Kairos News"""

    MEDIA_CANDIDATES = ["風向新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        return BaseMediaNewsCrawler._get_script_info(soup)["@graph"][5]

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="entry-content entry clearfix").text
        logger.debug(f"CONTENT:\n {content}")
        return content
