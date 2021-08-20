# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import pchome
from src.utils.struct import NewsStruct

logger = logging.getLogger(__name__)


TEST_DATA = namedtuple(
    typename="TEST_DATA",
    field_names=[
        "name",
        "link",
        "expected_output",
    ],
)

TEST_DATA_1 = TEST_DATA(
    name="pchome_1",
    link="https://news.pchome.com.tw/finance/cna/20210817/index-16291636203632218003.html",
    expected_output=NewsStruct(
        title="台積電開低壓抑指數 台股持續弱勢",
        content="\n\n            美股四大指數漲跌互見，蘋果尾盤黑翻紅再創新高，外資連2天期現貨翻多，蘋果相關概念股相對強勢，唯台積電開低下跌4元開出，壓抑指數以下跌17點、16841點開出。台股早盤以16841點、下跌17點開出，指數在平盤上下震盪，市場持續關注聯準會（Fed）釋出利率訊息、國際局勢、疫情變化，量能依舊低迷。台股今天開盤強勢指標包括航運三雄全面開高，再度成為盤面漲幅領先類股，電子類股中，光學鏡頭廠大立光、玉晶光、PA類股穩懋、漲價利多訊息的聯電、IC 設計類股相對強勢。昨天公布聯亞COVID-19疫苗EUA未過，衝擊聯亞藥股價持續跳水，跌幅近50%，100元關卡失守，早盤最低來到82.9元；另一家國產疫苗高端則開高，漲幅超過6%，表現兩樣情。\n          ",
        keywords=["COVID-19", "Fed", "台積電", "疫情", "疫苗", "聯電", "航運", "蘋果"],
        category=["新聞", "財經"],
        media="PChome新聞",
        datetime="2021-08-17 09:27:00",
        link="https://news.pchome.com.tw/finance/cna/20210817/index-16291636203632218003.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="pchome_2",
    link="https://news.pchome.com.tw/finance/cna/20210817/index-16291653018707918003.html",
    expected_output=NewsStruct(
        title="爭取EUA失利 聯亞藥股價再跳水大跌逾5成",
        content="\n\n            聯亞疫苗中和抗體效價偏低，EUA未通過，加上大股東持續賣股，負責充填的子公司聯亞藥股價繼昨天大跳水後，今天早盤再度重挫，跌幅一度超過5成，股價連2天腰斬跌破百元關卡。聯亞藥今天股價持續弱勢，早盤以116元，下跌54.53元、跌幅31.9%開出，賣壓持續出籠摜壓股價最低來到82.9元，跌幅一度擴大到51.3%，開盤半小時成交量已超過8000張。另一家國產疫苗廠高端將於23日起開打，開放預約首日超過30萬人預約成功，有近5成符合資格者搶約，高端疫苗預約踴躍，激勵高端股價強勢開高震盪走高，開盤半小時漲幅達8%。中央流行疫情指揮中心指揮官陳時中16日宣布，聯亞生技的COVID-19疫苗UB-612因中和抗體效價偏低，經專家審查認為未達緊急使用授權（EUA）標準，無法取得EUA。聯亞生技16日表示，目前國內臨床二期試驗持續進行，母公司將重新執行第三期臨床試驗的效益評估。海外臨床部分，UB-612疫苗於印度第三期臨床試驗計畫已獲印度政府核准，目前尚未執行。基於國內緊急使用授權（EUA）審查結果，對於印度第三期臨床試驗執行將再次審慎評估。聯亞生技指出，將向財團法人醫藥品查驗中心（CDE）及衛生福利部食品藥物管理署（TFDA）申訴，提議以Delta變異株同時比較UB-612與AZ疫苗所產生的抗體力價，並以原來的兩項統計標準進行免疫橋接試驗，客觀評估中和抗體保護力。食藥署指出，聯亞生技疫苗如果要另設一套標準，以最早在印度發現的Delta變異株比較，須提資料說服審查專家。\n          ",
        keywords=["COVID-19", "生技", "疫情", "疫苗", "陳時中"],
        category=["新聞", "財經"],
        media="PChome新聞",
        datetime="2021-08-17 09:55:01",
        link="https://news.pchome.com.tw/finance/cna/20210817/index-16291653018707918003.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return pchome.PChomeNewsCrawler()


@pytest.mark.parametrize(
    argnames="name, link, expected_output",
    argvalues=[tuple(t) for t in TEST_DATA_LIST],
    ids=[
        f"{t.name}, {t.link[:50]+'...' if len(t.link) > 50 else t.link}"
        for t in TEST_DATA_LIST
    ],
)
def test_get_info(
    newsCrawler,
    name,
    link,
    expected_output,
):
    output = newsCrawler.getInfo(link=link)
    assert NewsStruct.__2dict__(output) == NewsStruct.__2dict__(expected_output)
