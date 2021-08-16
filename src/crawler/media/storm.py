# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict
import json

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class StormNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for Strom News"""

    MEDIA_CANDIDATES = ["風傳媒"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 1-st element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[1].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n" f"{script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n" f"{script_info_dict}")
        return script_info_dict

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="article_content_inner").text
        logger.debug(f"CONTENT:\n {content}")
        return content
