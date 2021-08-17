# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union
import json

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TaroNewsNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for TaroNews News"""

    MEDIA_CANDIDATES = ["芋傳媒"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 1-st element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[2].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords_list = soup.find(
            "div", class_="entry-terms post-tags clearfix"
        ).find_all("a")
        keywords = [k.text for k in keywords_list]
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find(
            "div", class_="entry-content clearfix single-post-content"
        ).text
        logger.debug(f"CONTENT:\n {content}")
        return content
