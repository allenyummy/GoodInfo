# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import json
import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.media.crawler.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CTEENewsCrawler(BaseMediaCrawler):
    """Web Crawler for CTEE News"""

    MEDIA_CANDIDATES = ["工商時報"]
    CONTENT_ATTR_PATH = ".entry-content"

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.select_one(self.CONTENT_ATTR_PATH).text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:
        # use 4-th element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[3].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n" f"{script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n" f"{script_info_dict}")

        # keywords not in script_info_dict but in soup.
        # I don't get them. I just let them go because it's a special case.
        # Maybe after a while, I'll figure out how to resolve it in an elegant way.
        return script_info_dict
