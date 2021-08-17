# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class PTSNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for PTS News"""

    MEDIA_CANDIDATES = ["公視新聞"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords_list = soup.find(
            "ul", class_="list-unstyled tag-list d-flex flex-wrap"
        ).find_all("a")

        keywords = sorted(
            list(
                set([k.text.strip() for k in keywords_list if k.text.strip() != "..."])
            )
        )

        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    @staticmethod
    def _get_category(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        category = soup.find_all("li", class_="breadcrumb-item")
        category = [c.text.strip() for c in category]
        logger.debug(f"CATEGORY: {category}")
        return category

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("article", class_="post-article").text
        logger.debug(f"CONTENT:\n {content}")
        return content
