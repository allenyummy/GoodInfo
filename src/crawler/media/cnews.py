# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CNewsNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for CNews News"""

    MEDIA_CANDIDATES = ["匯流新聞網"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = soup.find("li", class_="date").text
        logger.debug(f"DATETIME: {datetime}")
        return datetime

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("article").text
        logger.debug(f"CONTENT:\n {content}")
        return content
