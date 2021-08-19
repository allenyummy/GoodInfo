# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Data structure

import json
import logging
from dataclasses import asdict, dataclass, field
from typing import List, Union

logger = logging.getLogger(__name__)


@dataclass
class GoodInfoStruct:
    股票代號: str
    股票名稱: str
    公司名稱: str = None
    英文簡稱: str = None
    產業別: str = None
    上市上櫃: str = None
    董事長: str = None
    總經理: str = None
    發言人: str = None
    代理發言人: str = None
    簽證會計師: str = None
    投資關係聯絡人: str = None

    def __repr__(self):
        return (
            f"[股票代號]: {self.股票代號}\n"
            f"[股票名稱]: {self.股票名稱}\n"
            f"[公司名稱]: {self.公司名稱}\n"
            f"[英文簡稱]: {self.英文簡稱}\n"
            f"[產業別]: {self.產業別}\n"
            f"[上市上櫃]: {self.上市上櫃}\n"
            f"[董事長]: {self.董事長}\n"
            f"[總經理]: {self.總經理}\n"
            f"[發言人]: {self.發言人}\n"
            f"[代理發言人]: {self.代理發言人}\n"
            f"[簽證會計師]: {self.簽證會計師}\n"
            f"[投資關係聯絡人]: {self.投資關係聯絡人}\n"
        )

    def __2json__(self):
        return json.dumps(
            asdict(self),
            ensure_ascii=False,
            indent=4,
        )

    def __2dict__(self):
        return json.loads(self.__2json__())


@dataclass
class GoogleNewsStruct:
    """Google News Data Structure"""

    title: str = field(
        default=None,
        metadata={"help": "News title."},
    )
    description: str = field(
        default=None,
        metadata={"help": "News description in abbrev. way"},
    )
    media: str = field(
        default=None,
        metadata={"help": "Media which releases news."},
    )
    datetime: str = field(
        default=None,
        metadata={"help": "Datetime in which news is released."},
    )
    link: str = field(
        default=None,
        metadata={"help": "News link."},
    )

    def __eq__(self, other) -> bool:
        return self.link == other.link

    def __repr__(self):
        return (
            "\n"
            f"[TITLE      ]: {self.title}\n"
            f"[DESCRIPTION]: {self.description}\n"
            f"[MEDIA      ]: {self.media}\n"
            f"[DATETIME   ]: {self.datetime}\n"
            f"[LINK       ]: {self.link}\n"
        )

    def __2json__(self):
        return json.dumps(
            asdict(self),
            ensure_ascii=False,
            indent=4,
        )

    def __2dict__(self):
        return json.loads(self.__2json__())


@dataclass
class NewsStruct:
    """News Data Structure"""

    title: str = field(
        default=None,
        metadata={"help": "News title."},
    )
    content: str = field(
        default=None,
        metadata={"help": "News content."},
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={"help": "News keywords."},
    )
    category: Union[str, List[str]] = field(
        default=None,
        metadata={"help": "News category."},
    )
    media: str = field(
        default=None,
        metadata={"help": "Media which releases news."},
    )
    datetime: str = field(
        default=None,
        metadata={"help": "Datetime in which news is released."},
    )
    link: str = field(
        default=None,
        metadata={"help": "News link."},
    )

    def __eq__(self, other) -> bool:
        return self.link == other.link

    def __repr__(self):
        return (
            "\n"
            f"[TITLE   ]: {self.title}\n"
            f"[CONTENT ]: {self.content}\n"
            f"[KEYWORDS]: {self.keywords}\n"
            f"[CATEGORY]: {self.category}\n"
            f"[MEDIA   ]: {self.media}\n"
            f"[DATETIME]: {self.datetime}\n"
            f"[LINK    ]: {self.link}\n"
        )

    def __2json__(self):
        return json.dumps(
            asdict(self),
            ensure_ascii=False,
            indent=4,
        )

    def __2dict__(self):
        return json.loads(self.__2json__())
