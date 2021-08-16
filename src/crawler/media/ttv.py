# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TTVNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for TTV News"""

    MEDIA_CANDIDATES = ["台視新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        raise NotImplementedError

    def _get_content(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError
