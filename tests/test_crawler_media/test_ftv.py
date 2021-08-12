# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ftv
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
    name="民視新聞_1",
    link="https://www.ftvnews.com.tw/news/detail/2021713W0276",
    expected_output=NewsStruct(
        title="解封概念股提早佈局！專家：留意「3大族群」起漲順序是重點",
        content="\n李永年表示，解封概念股有3大族群可以提前布局，分別是餐飲業、飯店業、旅遊業，這也分別是它們的起漲順序，雖然目前還在三級警戒，不過當警戒一解除，民眾能做的也是最簡單的事情就是到餐廳和親朋好友聚餐，再來才是飯店業，最後才是旅遊業，主要原因是台灣大部分的上市櫃旅行社都主攻國外旅遊市場，所以如果要等全球完全解封可能還有一段時間。第一波以「餐飲業」來看，投資人可以留意王品（2727）、瓦城（2729）以及經營85度C的美食-KY（2723）。（資料照／民視新聞）李永年指出，第一波以「餐飲業」來看，投資人可以留意王品（2727）、瓦城（2729）以及經營85度C的美食-KY（2723），會說美食-KY最主要是因為，85度C在美國與中國的營收相對穩定，門市來客數連5月走揚，雖然台灣實施三級警戒，但85度C在台灣的產品結構下有不少是來自蛋糕及麵包，影響相對來說較能受控制，所以復甦能力好，往後的基本面較能持續穩健。另外，第二波起漲的概念股就是「飯店業」，尤其是旗下既有飯店又有遊樂設施的六福（2705）、劍湖山（5701）等公司，會是民眾的首選，在股市的走勢也會比較吃香。而最後一波起漲的概念股，就是民眾最期盼能出國的「旅遊業」，李永年指出，像是雄獅（2731）、鳳凰（5706）等，不過全球疫情尚未平穩，短期之內沒辦法看得非常樂觀，加上台灣疫苗覆蓋率還未達到目標，國內旅遊也還沒能真正的解封，建議投資人先觀望，待台灣民眾大多都已完成疫苗接種時，可以再進場也不遲。《民視新聞網》提醒您：內容僅供參考，投資人於決策時應審慎評估風險，並就投資結果自行負責。\n",
        keywords=["財經", "微解封", "解封概念股", "餐飲", "飯店", "旅遊", "台股"],
        category="財經",
        media="民視新聞",
        datetime="2021-07-13T18:29:17+08:00",
        link="https://www.ftvnews.com.tw/news/detail/2021713W0276",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="民視新聞_2",
    link="https://www.ftvnews.com.tw/news/detail/2021721W0079",
    expected_output=NewsStruct(
        title="MCU市況續熱　新唐盤中漲停創新天價",
        content="\n受惠家電等市場需求強勁，加上晶圓代工與後段封測產能吃緊，第3季MCU市場依然維持供不應求態勢，產品價格也隨著成本增加不斷上漲。新唐（4919）等MCU族群在市場資金湧入下，推升股價紛紛走高，其中， 新唐股價強攻漲停，達新台幣147.5元，創新天價。至10時15分，凌通（4952）股價一度達94.3元，應廣（6716）達232元，九齊（6494）也達179元，同創歷史新高價。盛群（6202）股價一度漲停，達149元，逼近歷史最高價149.5元。其餘松翰（5471）與紘康（6457）今天股價也有不錯表現，松翰一度達119元，漲10元，漲幅逾9%，創近14年新高價。紘康一度達167元，漲8元，漲幅逾5%。（中央社）\n",
        keywords=["微控制器", "財經", "MCU", "新唐", "凌通", "應廣", "九齊", "盛群"],
        category="財經",
        media="民視新聞",
        datetime="2021-07-21T10:53:11+08:00",
        link="https://www.ftvnews.com.tw/news/detail/2021721W0079",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ftv.FTVNewsCrawler()


@pytest.mark.parametrize(
    argnames="name, link, expected_output",
    argvalues=[tuple(t) for t in [TEST_DATA_1, TEST_DATA_2]],
    ids=[
        f"{t.name}, {t.link[:50]+'...' if len(t.link) > 50 else t.link}"
        for t in [TEST_DATA_1, TEST_DATA_2]
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
