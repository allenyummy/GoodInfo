# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class UpMediaNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for UpMedia News"""

    MEDIA_CANDIDATES = ["上報"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="editor").text
        for script in soup.find("div", class_="editor").find_all("script"):
            if script.text in content:
                content = content.replace(script.text, "")
        logger.debug(f"CONTENT:\n {content}")
        return content
