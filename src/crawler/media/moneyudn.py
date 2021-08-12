# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import json
import logging
from typing import Dict

from bs4 import BeautifulSoup

from src.crawler.media.base import BaseMediaCrawler
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


class MoneyUDNNewsCrawler(BaseMediaCrawler):
    """Web Crawler for MoneyUDN News"""

    MEDIA_CANDIDATES = ["經濟日報"]
    CONTENT_ATTR_PATH = None

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    def _get_content(self, soup: BeautifulSoup) -> str:
        content = soup.find("div", id="article_body").text
        logger.debug(f"CONTENT:\n {content}")
        return content

    @staticmethod
    def _get_script_info(soup: BeautifulSoup) -> Dict[str, str]:
        def replace_all(text: str, replace: Dict[str, str]) -> str:
            for old_str, new_str in replace.items():
                text = text.replace(old_str, new_str)
            return text

        script_info_str = soup.find(
            "script",
            type="application/ld+json",
        ).string
        logger.debug(f"ORI_SCRIPT_INFO_STR:\n {script_info_str}")

        script_info_str = replace_all(
            script_info_str,
            {
                '//"interactionCount"': '"interactionCount"',
                "// 文章互動數": "",
                "// 高度， 有預設或是pgw的高度": "",
            },
        )
        logger.debug(f"REP_SCRIPT_INFO_STR:\n {script_info_str}")

        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict
