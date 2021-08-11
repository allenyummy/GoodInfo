# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.media.crawler.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class TechnewsNewsCrawler(BaseMediaCrawler):
    """Web Crawler for Technews News"""

    MEDIA_CANDIDATES = ["科技新報", "財經新報"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        raise NotImplementedError

    def _get_content(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError
