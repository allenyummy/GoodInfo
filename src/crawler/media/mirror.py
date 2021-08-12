# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class MirrorNewsCrawler(BaseMediaCrawler):
    """Web Crawler for Mirror News"""

    MEDIA_CANDIDATES = ["鏡週刊"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content_list = soup.find_all("p", class_="g-story-paragraph")
        content = "\n".join([s.text for s in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str], soup: BeautifulSoup
    ) -> Union[List[str], None]:
        keywords = soup.find(attrs={"name": "news_keywords"}).get("content").split(",")
        keywords = [k.strip() for k in keywords]
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords
