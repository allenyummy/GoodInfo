# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get GoodInfo

import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from config import (
    上市公司_欄位,
    上市公司_終止列,
    上市公司_網址,
    上市公司_起始列,
    上櫃公司_欄位,
    上櫃公司_終止列,
    上櫃公司_網址,
    上櫃公司_起始列,
    台灣股市資訊網_基本資料_網址,
)


# 臺灣證券交易所
# 爬上市/上櫃公司的名稱和股票代號
def get_code_name():

    ret = dict()

    for 網址, 起始列, 終止列, 欄位 in zip(
        [上市公司_網址, 上櫃公司_網址],
        [上市公司_起始列, 上櫃公司_起始列],
        [上市公司_終止列, 上櫃公司_終止列],
        [上市公司_欄位, 上櫃公司_欄位],
    ):

        print(網址, 起始列, 終止列, 欄位)
        res = requests.get(網址)
        soup = BeautifulSoup(res.text, "lxml")
        data = soup.select_one("table.h4")
        df = pd.read_html(data.prettify())[0]

        for d in df.iloc[起始列:終止列, 欄位]:
            tmp = d.split()
            code = tmp[0]
            name = tmp[1]
            ret[code] = {"股票代號": code, "股票名稱": name}

    return ret


# Goodinfo
# 爬上市上櫃公司的基本資料
def get_basic(code):

    URL = f"{台灣股市資訊網_基本資料_網址}?STOCK_ID={code}"
    res = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            " AppleWebKit/605.1.15"
            " (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        },
    )
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "lxml")
    data = soup.select_one("table.b1.p4_6.r10")
    df = pd.read_html(data.prettify())[0]

    return {
        "股票代號": df[1][1],
        "股票名稱": df[3][1],
        "公司名稱": df[1][3],
        "英文簡稱": df[1][4],
        "產業別": df[1][2],
        "上市/上櫃": df[3][2],
        "董事長": df[1][11],
        "總經理": df[1][12],
        "發言人": df[1][13],
        "代理發言人": df[1][14],
        "簽證會計師": df[1][27],
        "投資關係聯絡人": df[1][28],
    }


def readJson(infile):
    with open(infile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    return data


def writeJson(data, outfile):
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
