# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get GoodInfo

import json
import random
import time
from typing import Dict

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

import src.config as cf
from src.utils.struct import GoodInfoStruct, dict2GoodInfoStruct


# 臺灣證券交易所
# 爬上市/上櫃公司的名稱和股票代號
def get_code_name() -> Dict[str, GoodInfoStruct]:

    data = dict()

    for 網址, 起始列, 終止列, 欄位 in zip(
        [cf.上市公司_網址, cf.上櫃公司_網址],
        [cf.上市公司_起始列, cf.上櫃公司_起始列],
        [cf.上市公司_終止列, cf.上櫃公司_終止列],
        [cf.上市公司_欄位, cf.上櫃公司_欄位],
    ):

        print(網址, 起始列, 終止列, 欄位)
        res = requests.get(網址)
        soup = BeautifulSoup(res.text, "lxml")
        retrieved = soup.select_one("table.h4")
        df = pd.read_html(retrieved.prettify())[0]

        for d in df.iloc[起始列:終止列, 欄位]:
            tmp = d.split()
            code = tmp[0]
            name = tmp[1]
            data[code] = GoodInfoStruct(股票代號=code, 股票名稱=name)

    return data


# Goodinfo
# 爬上市上櫃公司的基本資料
def get_basic(code: str) -> GoodInfoStruct:

    URL = f"{cf.台灣股市資訊網_基本資料_網址}?STOCK_ID={code}"
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
    retrieved = soup.select_one("table.b1.p4_6.r10")
    df = pd.read_html(retrieved.prettify())[0]

    return GoodInfoStruct(
        股票代號=df[1][1],
        股票名稱=df[3][1],
        公司名稱=df[1][3],
        英文簡稱=df[1][4],
        產業別=df[1][2],
        上市上櫃=df[3][2],
        董事長=df[1][11],
        總經理=df[1][12] if not pd.isna(df[1][12]) else None,
        發言人=df[1][13] if not pd.isna(df[1][13]) else None,
        代理發言人=df[1][14] if not pd.isna(df[1][14]) else None,
        簽證會計師=df[1][27] if not pd.isna(df[1][27]) else None,
        投資關係聯絡人=df[1][28] if not pd.isna(df[1][28]) else None,
    )


def get_all_basic(
    data: Dict[str, GoodInfoStruct],
    outfile: str,
) -> Dict[str, GoodInfoStruct]:

    for i, code in enumerate(
        tqdm(
            data,
            total=(len(data)),
            desc="Get Basic Info",
        )
    ):

        try:
            if data[code].公司名稱:
                continue
            basic = get_basic(code)

        except Exception as e:
            print(e)
            # Write file and exit
            writeJson(data, outfile)
            break

        else:
            data[code] = basic
            # Write every 10 data into files
            if i > 0 and i % 10 == 0:
                writeJson(data, outfile)
                print(f"Write2Json: {i-10} ~ {i}.")

        time.sleep(random.randint(15, 20))

    writeJson(data, outfile)
    return data


def readJson(infile: str) -> Dict[str, GoodInfoStruct]:

    with open(infile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    # transform to GoodInfoStruct
    for code in data:
        data[code] = dict2GoodInfoStruct(data[code])

    return data


def writeJson(data: Dict[str, GoodInfoStruct], outfile: str):

    tmp = data.copy()

    # transform to dict
    for code in tmp:
        if isinstance(tmp[code], GoodInfoStruct):
            tmp[code] = tmp[code].__2dict__()

    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(tmp, f, ensure_ascii=False, indent=4)
        f.close()
