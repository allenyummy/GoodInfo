# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import json
import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class UDNNewsCrawler(BaseMediaCrawler):
    """Web Crawler for UDN News"""

    MEDIA_CANDIDATES = ["聯合新聞網"]
    CONTENT_ATTR_PATH = ".article-content__editor"

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.select_one(self.CONTENT_ATTR_PATH).text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:
        # list of dictionary
        script_info_str = soup.find("script", type="application/ld+json").string

        # use first element (0-indexed)
        script_info_dict = json.loads(script_info_str)[0]
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict
