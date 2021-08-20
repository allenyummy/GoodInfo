# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import rti
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
    name="中央廣播電臺_1",
    link="https://www.rti.org.tw/news/view/id/2108692",
    expected_output=NewsStruct(
        title="破半年線後跌勢未止  台股盤中失守16800點",
        content="\n\n\n台股17日盤中失守16800點。 (資料照片／中央社)\n\n電子股表現不振，台北股市今天(17日)開盤後依舊呈現震盪走低的格局，盤中一度跌破16800點，截至上午11時，成交量低於新台幣2000億元，持續量縮格局，法人認為，市場缺乏主流股挺身而出，短線恐怕沒有止跌訊號浮現。\n與疫情相關的生技股表現強勁，高端疫苗、生華科大漲，唯獨緊急使用授權(EUA)未過的聯亞藥開盤一度下挫至82.9元為近期新低。\n截至11時10分，台北股市下跌57.15點，來到16801.62點，成交金額新台幣1359.72億元。\n分析師表示，由於美國科技股遲遲未能止穩，台股欲振乏力，且在跌破半年線16956點之後仍無反彈企圖，雖有金融、航運等族群零星點火，但市場信心薄弱，沒有主流股挺身而出之下，短線上無止跌訊號浮現。\n分析師表示，隨著美國兩黨基建計畫達成協議，有助刺激經濟，加上第2季財報數據亮眼，國際大廠多對下半年展望正向，激勵美股持續高檔走勢。不過，台灣方面MSCI季度調整台灣權重再次調降，且政策面對市場不友善，造成人氣退潮、成交量能縮減，操作難度增加。\n",
        keywords=["台股"],
        category="財經",
        media="中央廣播電臺",
        datetime="2021-08-17T11:10:43+08:00",
        link="https://www.rti.org.tw/news/view/id/2108692",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="中央廣播電臺_2",
    link="https://www.rti.org.tw/news/view/id/2108706",
    expected_output=NewsStruct(
        title="馬英九：五倍券為德不卒 應發現金紓困",
        content="\n\n\n前總統馬英九（前中）17日表示，五倍券為德不卒，應該發現金，因為現在最需要紓困的是基層服務業，很多商家已無法營業，沒有收入，紓困要針對真正需要的民眾才有意義。 (圖：中央社)\n\n行政院擬發振興五倍券促進內需消費，前總統馬英九今天(17日)表示，五倍券為德不卒，應該發現金，因為現在最需要紓困的是基層服務業，很多商家已無法營業，沒有收入，紓困要針對真正需要的民眾才有意義。\n針對目前阿富汗情勢，台灣民間出現「今日阿富汗，明日台灣」的聲音，憂慮美國也會拋棄台灣。馬英九表示，阿富汗不能跟台灣相比，歡迎外國援助台灣，但台灣也要有自我防衛的力量。\n馬英九上午出席國民黨立委陳以信召開的「飛虎：陳納德將軍與美籍志願大隊」新書發表會。針對政府拍板，朝全民免費獲取五倍券方向規劃，馬英九在會前受訪表示，紓困一定要對症下藥，針對真正需要的民眾紓困才有意義，所以他認為應該發現金比較好。\n馬英九指出，五倍券與當年的消費券近似，但還是為德不卒，因為現在最需要紓困的是基層服務業，很多商家都已無法營業，沒有收入。但工業、貿易情況還不錯，所以今年經濟還可以維持正成長。\n外界認為，當年馬政府發行消費券遭到批評，如今蔡政府規劃全民免費領五倍券是還馬英九公道。馬英九表示，他非常感謝大家說要還馬英九公道，但是這不重要，最重要的是要讓民眾有公道。\n",
        keywords=["馬英九", "振興券", "五倍券"],
        category="政治",
        media="中央廣播電臺",
        datetime="2021-08-17T12:34:16+08:00",
        link="https://www.rti.org.tw/news/view/id/2108706",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return rti.RTINewsCrawler()


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
