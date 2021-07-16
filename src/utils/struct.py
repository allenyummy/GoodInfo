# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Data structure

import logging
from dataclasses import dataclass, field
from typing import Dict, List

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

    def __2dict__(self):
        return {
            "股票代號": self.股票代號,
            "股票名稱": self.股票名稱,
            "公司名稱": self.公司名稱,
            "英文簡稱": self.英文簡稱,
            "產業別": self.產業別,
            "上市上櫃": self.上市上櫃,
            "董事長": self.董事長,
            "總經理": self.總經理,
            "發言人": self.發言人,
            "代理發言人": self.代理發言人,
            "簽證會計師": self.簽證會計師,
            "投資關係聯絡人": self.投資關係聯絡人,
        }


def dict2GoodInfoStruct(ipt: Dict[str, str]):
    return GoodInfoStruct(
        股票代號=ipt["股票代號"],
        股票名稱=ipt["股票名稱"],
        公司名稱=ipt["公司名稱"],
        英文簡稱=ipt["英文簡稱"],
        產業別=ipt["產業別"],
        上市上櫃=ipt["上市上櫃"],
        董事長=ipt["董事長"],
        總經理=ipt["總經理"],
        發言人=ipt["發言人"],
        代理發言人=ipt["代理發言人"],
        簽證會計師=ipt["簽證會計師"],
        投資關係聯絡人=ipt["投資關係聯絡人"],
    )


@dataclass
class NewsDetailsStruct:
    def __repr__(self):
        pass

    def __2dict__(self):
        pass


@dataclass
class NewsStruct:
    股票名稱: str
    新聞: List[NewsDetailsStruct] = field(default_factory=list)

    def __repr__(self):
        pass

    def __2dict__(self):
        pass


@dataclass
class DataStruct:
    updatetime: str
    version: str
    data: List[NewsStruct]
    pass
