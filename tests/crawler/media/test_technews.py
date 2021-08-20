# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import technews
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
    name="財經新報_1",
    link="https://finance.technews.tw/2021/06/09/caswell-6416-202105-financial-report/",
    expected_output=NewsStruct(
        title="瑞祺電通5月營收月增28.3%",
        content="\n\n\n\n\n\n瑞祺電通（6416）公布 5 月合併營收 3.86 億元，較上（4）月成長 28.3%，與去年同期相比為年增 -14.5%；累計其今年前 5 月營收為 19.27 億元，較去年同期增加 -10.1%。\n\n\n",
        keywords=None,
        category=None,
        media="財經新報",
        datetime=None,
        link="https://finance.technews.tw/2021/06/09/caswell-6416-202105-financial-report/",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="財經新報_2",
    link="https://finance.technews.tw/2021/07/09/mvi-2342-202106-financial-report/",
    expected_output=NewsStruct(
        title="茂矽6月營收1.67 億元",
        content="\n\n\n\n\n\n茂矽（2342）今（9）日公布 6 月營收，達 1.67 億元，較 5 月成長 -2.9%，較去年同期成長 -9.4%，累計前 6 月營收為 8.89 億元，年增 -2.8%。\n\n\n",
        keywords=None,
        category=None,
        media="財經新報",
        datetime=None,
        link="https://finance.technews.tw/2021/07/09/mvi-2342-202106-financial-report/",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return technews.TechnewsNewsCrawler()


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
