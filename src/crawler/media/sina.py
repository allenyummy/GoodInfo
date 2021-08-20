# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class SINANewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for SINA News"""

    MEDIA_CANDIDATES = ["新浪新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", itemprop="articleBody").text
        for script in soup.find("div", itemprop="articleBody").find_all("script"):
            if script.text in content:
                content = content.replace(script.text, "")
        logger.debug(f"CONTENT:\n {content}")
        return content
