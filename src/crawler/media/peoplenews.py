# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class PeopleNewsNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for PeopleNews News"""

    MEDIA_CANDIDATES = ["民報"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords = None
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", itemprop="articleBody").text
        logger.debug(f"CONTENT:\n {content}")
        return content
