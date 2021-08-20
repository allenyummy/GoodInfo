# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class LTNNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for LTN News"""

    MEDIA_CANDIDATES = ["自由時報電子報", "自由財經"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = list()
        for c in soup.find("div", class_="text").find_all("p"):
            if c.has_attr("class"):
                continue
            content_list.append(c)

        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}\n")
        return content
