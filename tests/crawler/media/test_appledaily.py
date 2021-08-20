# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import appledaily
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
    name="蘋果日報_1",
    link="https://tw.appledaily.com/property/20210722/X7R2YYQTSJA3FMCB642SBQY5JM/",
    expected_output=NewsStruct(
        title="類股輪動格局　航運股恐持續弱勢",
        content="昨天台股開高走低，在航運股拖累下指數終場下跌69點，跌幅0.4%，指數收於17458點，成交量為6131億元。台新投顧副總黃文清表示，指數暫跌至月線17735點以下，預計短線指數震盪為主，操作上，可先留意中小型股。黃文清表示，短線指數震盪，類股持續輪動，航運股恐偏弱格局，汽車相關零組件、車用電子、蘋果概念股可持續留意。投資建議，考量華為之高階手機市場缺口，以及市場對5G的換機強勁需求，將有利蘋果新機銷售，因此初步預估樂觀，給出較往年提高兩成的下單量，亦看好2H21蘋果將較中系手機品牌有更好的成長表現。相關個股：台積電(2330)、晶技(3042)、同欣電(6271)、穩懋(3105)。至於近來震盪幅度相當大的航運股，法人分析，航運股股價修正逾3成，航運股頻頻利多不漲，長榮的融資餘額仍高達二十四萬張，預計將持續融資減肥，對股價形成向下壓力，考慮未來展望偏保守，建議逢高調節，獲利入袋了。（林彤婕／台北報導）航運股台股",
        keywords=[
            "航運股",
            "台股",
            "mt_投資",
            "mt_理財",
            "mt_AUTO_hierarchy_金融",
            "mt_AUTO_node_股票",
        ],
        category="財經地產",
        media="蘋果日報",
        datetime="2021-07-21T21:29:00Z",
        link="https://tw.appledaily.com/property/20210722/X7R2YYQTSJA3FMCB642SBQY5JM/",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="蘋果日報_2",
    link="https://tw.appledaily.com/property/20200616/TYDZD67VFHQM3PKCZDL6ZL4TCA/",
    expected_output=NewsStruct(
        title="合一解盲成功股價跳空漲停　遭爆有內線交易嫌疑",
        content="合一生技中天生技糖尿病",
        keywords=[
            "合一生技",
            "中天生技",
            "糖尿病",
            "mt_投資",
            "mt_AUTO_hierarchy_保健品藥",
            "mt_AUTO_node_保健",
            "cat_財經",
        ],
        category="財經地產",
        media="蘋果日報",
        datetime="2020-06-16T01:13:00Z",
        link="https://tw.appledaily.com/property/20200616/TYDZD67VFHQM3PKCZDL6ZL4TCA/",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return appledaily.AppleDailyNewsCrawler()


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
