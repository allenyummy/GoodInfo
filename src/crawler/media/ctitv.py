# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class CTITVNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for CTITV News"""

    MEDIA_CANDIDATES = ["中天新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords_list = soup.find("div", class_="tagcloud").find_all("a")
        keywords = [k.text for k in keywords_list]
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find("div", class_="post-content description").find_all("p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
