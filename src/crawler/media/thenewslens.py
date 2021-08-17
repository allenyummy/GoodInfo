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


class TheNewsLensNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for TheNewsLens News"""

    MEDIA_CANDIDATES = ["關鍵評論網"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 3-rd element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[3].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        whyneedknow = soup.find("header", class_="WhyNeedKnow").find("p").text
        content = soup.find("article", itemprop="articleBody").text
        content = whyneedknow + "\n" + content
        logger.debug(f"CONTENT:\n {content}")
        return content
