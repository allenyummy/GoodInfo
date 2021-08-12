# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class ChinatimesNewsCrawler(BaseMediaCrawler):
    """Web Crawler for Chinatimes News"""

    MEDIA_CANDIDATES = ["中時新聞網"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find(class_="article-body", itemprop="articleBody").text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_link(script_info: Dict[str, str]) -> str:
        return script_info.get("mainEntityOfPage").get("@id")
