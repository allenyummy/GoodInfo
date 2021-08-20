# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaNewsCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class WorldJournalNewsCrawler(BaseMediaNewsCrawler):
    """Web Crawler for WorldJournal News"""

    MEDIA_CANDIDATES = ["世界新聞網"]

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(
        self,
        soup: BeautifulSoup,
    ) -> str:

        paragrah = soup.find("div", class_="article-content__paragraph")

        content_list = list()
        for content_cand in paragrah.find_all("p"):
            if content_cand.text in ["上一則", "下一則"]:
                continue
            content_list.append(content_cand)

        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
