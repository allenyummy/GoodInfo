# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TaiwanHotNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for TaiwanHot News"""

    MEDIA_CANDIDATES = ["台灣好新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords = None
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = soup.find("span", class_="post_time").text.strip()
        logger.debug(f"DATETIME: {datetime}")
        return datetime

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find("article").find_all("p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
