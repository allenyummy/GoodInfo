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


class RTINewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for RTI News"""

    MEDIA_CANDIDATES = ["中央廣播電臺"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # list of dictionary
        script_info_str = soup.find("script", type="application/ld+json").string

        # use first element (0-indexed)
        script_info_dict = json.loads(script_info_str)[0]
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("article").text
        logger.debug(f"CONTENT:\n {content}")
        return content
