# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TTVNewsCrawler(BaseMediaCrawler):
    """Web Crawler for TTV News"""

    MEDIA_CANDIDATES = ["台視新聞"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        raise NotImplementedError

    def _get_content(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError
