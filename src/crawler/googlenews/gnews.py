# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get google news of companies from goodinfo

import logging
from typing import List, Union

from src.config import MEDIA_URL
from src.utils.struct import GoogleNewsStruct
from src.crawler.googlenews import GoogleNews

logger = logging.getLogger(__name__)


class GoogleNewsCrawler:
    """Web Crawler for Google News"""

    def __init__(self):
        """
        Init GoogleNewsCrawler.
        """

        self.crawler = GoogleNews(lang="zhtw", encode="utf-8")

    def getInfo(self, query: str) -> List[GoogleNewsStruct]:
        """
        Get news from google.

        Args:
            query: It's a query to search related news.
                   Multiple queries coud be concatted by space.
        Type:
            query: string
        Return:
            List of google news.
            rtype: List of GoogleNewsStruct
        """

        self.crawler.clear()
        ret = list()

        self.crawler.search(query)
        results = self.crawler.results(sort=True)

        for res in results:

            media = self._get_media(res["link"])

            if not media:
                raise ValueError(
                    f"MediaNewsCrawler doesn't support {res['link']}"
                    f", you should add this link or media {res['media']}"
                )

            gns = GoogleNewsStruct(
                title=res["title"],
                description=res["desc"],
                media=media,
                datetime=res["datetime"].strftime("%Y/%m/%d %H:%M:%S")
                if res["datetime"]
                else None,
                link=res["link"],
            )

            if gns not in ret:
                ret.append(gns)

        return ret

    @staticmethod
    def _get_media(link: str) -> Union[str, None]:
        """
        Correct media by checking links.
        It's for internal use.

        Args:
            link: News link.
        Type:
            link: string
        Return:
            Media name or Nothing (because it's never in config.MEDIA_URL)
            rtype: string or None
        """

        for media, url in MEDIA_URL.items():
            if url in link:
                return media
        return None


if __name__ == "__main__":

    # import random
    # import sys

    # from tqdm import tqdm

    # from src.goodinfo import readJson

    # # """ Get company from GoodInfo """
    # goodinfo = readJson("out/company.json")
    # goodinfo_values = list(goodinfo.values())
    # random.shuffle(goodinfo_values)

    # """ Init GoogleNewsCrawler """
    # gnc = GoogleNewsCrawler()

    # """ Get news from cache file """
    # gnc.getCache("out/googlenews.json")
    # print(f"Now #{len(gnc.results)}")

    # """ Get news from google """
    # for i, g in enumerate(
    #     tqdm(
    #         goodinfo_values,
    #         total=(len(goodinfo_values)),
    #         desc="Get Google News of Company",
    #     )
    # ):
    #     print(g.股票名稱)
    #     gnc.getInfo(g.股票名稱, g.股票代號, pages=[1])
    #     # gnc.writeJson(gnc.results, "out/googlenews.json")

    #     if i == 39:
    #         sys.exit()

    gnc = GoogleNewsCrawler()
    results = gnc.getInfo(query="台積電 2330")
    # results = gnc.results()
    print(results[0])
    # for res in results:
    #     print(res)
    #     print()

    # print("=====")
    # gn.clear()
    # query = ["創意", "3443"]
    # gn.search(f"{' '.join(query)}")
    # results = gn.results()
    # for res in results:
    #     print(res)
    #     print()
