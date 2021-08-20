# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ebc
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
    name="東森財經新聞_1",
    link="https://fnc.ebc.net.tw/FncNews/stock/127025",
    expected_output=NewsStruct(
        title="個股：疫情催化醫療服務端導入，醫揚(6569)機器人國內外市場拓展加速",
        content="\n\n \n【往下看更多】\r\n            ►客戶愛玩隔日沖 券商分點Google評論遭洗版  網笑：韭菜取暖大會\r\n            ►航運、鋼鐵強勢領軍 台股開低走高跌幅收斂\r\n            ►航運、電子咕嚕咕嚕 台股量縮失守季線 網哀一片：人走茶涼\n",
        keywords=None,
        category="stock",
        media="東森財經新聞",
        datetime="2020/10/27 12:05",
        link="https://fnc.ebc.net.tw/FncNews/stock/127025",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="東森財經新聞_2",
    link="https://fnc.ebc.net.tw/FncNews/stock/127025",
    expected_output=NewsStruct(
        title="產業：歐美報復性消費＋國際油價漲，紡織業大利多，化纖報價釀新一波漲勢",
        content="\n\n \n【往下看更多】\r\n            ►興櫃：樂意上半年營收增逾兩成，獲韓《失落的方舟：LOST ARK》代理權\r\n            ►興櫃：圓點奈米(6797)上半年獲利大增3.8倍，EPS 17.06元\r\n            ►個股：訂單回流＋新品效益，精聯H1 EPS 0.78元，創11年新高，H2旺季不看淡\n",
        keywords=None,
        category="else",
        media="東森財經新聞",
        datetime="2021/06/03 14:05",
        link="https://fnc.ebc.net.tw/fncnews/else/135466",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ebc.EBCNewsCrawler()


@pytest.mark.parametrize(
    argnames="name, link, expected_output",
    argvalues=[tuple(t) for t in TEST_DATA_LIST],
    ids=[
        f"{t.name}, {t.link[:50]+'...' if len(t.link) > 50 else t.link}"
        for t in TEST_DATA_LIST
    ],
)
@pytest.mark.skip(reason="EBC locks their contents !")
def test_get_info(
    newsCrawler,
    name,
    link,
    expected_output,
):
    output = newsCrawler.getInfo(link=link)
    assert NewsStruct.__2dict__(output) == NewsStruct.__2dict__(expected_output)
