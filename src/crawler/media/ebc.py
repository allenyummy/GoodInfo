# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import json
import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class EBCNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for EBC News"""

    MEDIA_CANDIDATES = ["東森財經新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 1-st element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[1].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="origin-style web-content").text
        logger.debug(f"CONTENT: \n {content}\n")
        return content
