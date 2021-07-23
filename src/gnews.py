# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get google news of companies from goodinfo

import json
import logging
import time
from dataclasses import dataclass, field
from typing import List, Union

from GoogleNews import GoogleNews

from src.base_crawler import BaseCrawler
from src.config import MEDIA_URL

logger = logging.getLogger(__name__)


@dataclass
class GoogleNewsStruct:
    """GoogleNews Data Structure"""

    company: List[str] = field(
        default_factory=list,
        metadata={
            "help": "Companies that exist in the news."
            "The argument may not contain all companies in the news"
            "because I add a company in the argument"
            "when the news GoogleNewsCrawler find is same as the previous one"
            "that has already been in List[GoogleNewsStruct]."
        },
    )
    title: str = field(
        default=None,
        metadata={"help": "News title."},
    )
    link: str = field(
        default=None,
        metadata={"help": "News link."},
    )
    description: str = field(
        default=None,
        metadata={"help": "News description in abbrev. way"},
    )
    media: str = field(
        default=None,
        metadata={"help": "Media from which releases news."},
    )
    datetime: str = field(
        default=None,
        metadata={"help": "Datetime in which news is released."},
    )

    def __eq__(self, other) -> bool:
        return self.link == other.link

    def __repr__(self):
        return (
            f"[COMPANY]: {self.company}\n"
            f"[MEDIA]: {self.media}\n"
            f"[TITLE]: {self.title}\n"
            f"[LINK]: {self.link}\n"
            f"[DESC]: {self.description}\n"
            f"[TIME]: {self.datetime}\n"
        )

    def __class2dict__(self) -> dict:
        return {
            "company": self.company,
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "media": self.media,
            "datetime": self.datetime,
        }

    @classmethod
    def __dict2class__(cls, ipt: dict) -> object:
        return cls(
            company=ipt["company"],
            title=ipt["title"],
            link=ipt["link"],
            description=ipt["description"],
            media=ipt["media"],
            datetime=ipt["datetime"],
        )


class GoogleNewsCrawler(BaseCrawler):
    """Web Crawler for Google News"""

    def __init__(self):
        """
        Init GoogleNewsCrawler.

        Return nothing but keep recording results to self._results.
        Get results by calling object_of_GoogleNewsCrawler.results.
        """

        self.crawler = GoogleNews(lang="zhtw", encode="utf-8")
        self._results = list()  # internal use

    def getInfo(
        self,
        company: str,
        other_keywords: str,
        pages: List[int],
    ) -> List[GoogleNewsStruct]:
        """
        Get news from google.

        Args:
            company        : Company from which you want to get news.
                             It's one of keywords to search news.
            other_keywords : Other keywords that you want to search news.
                             Here, I use stock code of company as a keyword.
            pages          : Search pages. Noted that it's 1-indexed.
        Type:
            company        : string
            other_keywords : string
            pages          : list of integer
        Return:
            List of google news.
            rtype: List of GoogleNewsStruct
            The obtained news are also collected into self._results.
        """

        self.crawler.search(f"{company} {other_keywords}")

        ret = list()
        for p_id in pages:  # pages is 1-indexed
            self.crawler.clear()
            self.crawler.get_page(p_id)
            results = self.crawler.results(sort=True)

            logger.debug(f"page, size: {p_id} {len(results)}")

            for res in results:
                gns = GoogleNewsStruct(
                    company=[company],
                    title=res["title"],
                    link=res["link"],
                    description=res["desc"],
                    media=self._correct_media(res["link"]),
                    datetime=res["datetime"].strftime("%Y/%m/%d %H:%M:%S")
                    if res["datetime"]
                    else None,
                )
                if gns not in ret:
                    ret.append(gns)
                    logger.debug(gns)

            time.sleep(30)

        # collect data into self._results
        self._results = self.merge(self._results, ret)
        # return data only for the input
        return ret

    def getCache(self, infile: str) -> List[GoogleNewsStruct]:
        """
        Get news from cache file.

        Args:
            infile: Cache file.
        Type:
            infile: string
        Return:
            List of google news.
            rtype: List of GoogleNewsStruct
            The obtained news are also collected into self._results.
        """

        cache_data = self.readJson(infile)
        logger.debug("cache data size: len()")

        # collect data into self._results
        self._results = self.merge(self._results, cache_data)
        # return data only for the input
        return cache_data

    @property
    def results(self) -> List[GoogleNewsStruct]:
        """
        Results of news from google and cache file.
        It's an API for external use.
        """

        return self._results

    def clear(self):
        """
        Clean self._results.
        """

        self._results = list()

    @staticmethod
    def _correct_media(link: str) -> Union[str, None]:
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
        else:
            return None

    @staticmethod
    def merge(
        data1: List[GoogleNewsStruct],
        data2: List[GoogleNewsStruct],
    ) -> List[GoogleNewsStruct]:
        """
        Merge two lists of GoogleNewsStruct.
        It's often used when merging self._results and latest news information.

        Args:
            data1: Data of google news.
            data2: Data of google news.
        Type:
            data1: List of GoogleNewsStruct
            data2: List of GoogleNewsStruct
        Return:
            A merged version of google news.
            rtype: List of GoogleNewsStruct
        """

        if not data1 or not data2:
            logger.debug("One of inputs is empty, just return the other")
            return data1 or data2

        ret = data1.copy()
        for d in data2:

            try:
                idx = ret.index(d)

            except ValueError:
                ret.append(d)

            else:
                ori_company = ret[idx].company
                tar_company = d.company
                merge_company = list(set(ori_company + tar_company))
                ret[idx].company = merge_company

        return ret

    @staticmethod
    def readJson(infile: str) -> List[GoogleNewsStruct]:
        """
        Read json file.

        Args:
            infile: Input file.
        Type:
            infile: string
        Return:
            Google news.
            rtype: List of GoogleNewsStruct
        """

        with open(infile, "r", encoding="utf-8") as f:
            tmp = json.load(f)
            f.close()

        ret = [GoogleNewsStruct().__dict2class__(t) for t in tmp if isinstance(t, dict)]
        return ret

    @staticmethod
    def writeJson(data: List[GoogleNewsStruct], outfile: str) -> None:
        """
        Write json file.

        Args:
            data: Data of google news.
            outfile: Output file.
        Type:
            data: List of GoogleNewsStruct
            outfile: string
        Return:
            None
        """

        tmp = data.copy()
        out = [t.__class2dict__() for t in tmp if isinstance(t, GoogleNewsStruct)]

        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=4)
            f.close()


if __name__ == "__main__":

    import random
    import sys

    from tqdm import tqdm

    from src.goodinfo import readJson

    """ Get company from GoodInfo """
    goodinfo = readJson("out/company.json")
    goodinfo_values = list(goodinfo.values())
    random.shuffle(goodinfo_values)

    """ Init GoogleNewsCrawler """
    gnc = GoogleNewsCrawler()

    """ Get news from cache file """
    gnc.getCache("out/googlenews.json")
    print(f"Now #{len(gnc.results)}")

    """ Get news from google """
    for i, g in enumerate(
        tqdm(
            goodinfo_values,
            total=(len(goodinfo_values)),
            desc="Get Google News of Company",
        )
    ):
        print(g.股票名稱)
        gnc.getInfo(g.股票名稱, g.股票代號, pages=[1])
        gnc.writeJson(gnc.results, "out/googlenews.json")

        if i == 39:
            sys.exit()
