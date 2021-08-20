# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import cts
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
    name="華視新聞_1",
    link="https://news.cts.com.tw/cts/money/202108/202108162053145.html",
    expected_output=NewsStruct(
        title="台股下跌40點開出 直接摜破半年線 - 華視新聞網",
        content="\n\n\n\n\n\n\n\n\n綜合報導  / 台北市 \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n台股的半年線保衛戰要宣告失守了嗎？今(16)日大盤以下跌40點開出，直接跌破半年線，盤中大跌超過200點，失守1萬6千800點關卡，最低殺到1萬6千773點。一早航運與鋼鐵扮演撐盤要角，無奈盤中殺聲再起，三雄也由紅翻黑，只剩下長榮獨撐大局，盤面上電纜造紙光電無一倖免，一片綠油油，連金融股都大跌將近2%，午盤跌幅稍微收斂，但仍在百分之1左右，約180點上下，台股接連摜破季線、半年線，技術面走空，多頭棄械，造成市場信心崩盤，台股已經連跌8天，最大跌點高達850點。\n\n\n\n\r\n                                新聞來源：華視新聞\r\n                            \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
        keywords=["台股"],
        category="財經",
        media="華視新聞",
        datetime="2021-08-16T15:26:00+08:00",
        link="https://news.cts.com.tw/cts/money/202108/202108162053145.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="華視新聞_2",
    link="https://news.cts.com.tw/cts/money/202107/202107282051061.html",
    expected_output=NewsStruct(
        title="一度重挫370點 航運股拉尾盤守住萬七 - 華視新聞網",
        content="\n\n\n\n\n\n\n\n\n王源澤 薛松乾 報導  / 台北市 \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n台股自從站上萬八之後，就不斷回檔。今(28)日盤中一度重挫超過370點，摜破1萬6千900點大關。不過還好航運拉尾盤，終場收在1萬7千135.22點，跌幅百分之0.78。雖然勉強站穩萬七，但盤面上還是一片綠油油，只有百貨跟運輸類股撐盤。分析師認為，台股受到中國股市影響，不過隨著航運股回穩，半導體止跌，未來如果反彈到季線以上，還是有多頭機會。開盤就殺聲隆隆，早盤一度下挫超過370點，摜破16900點關卡，不過隨後跌跌不休的航運股，買盤接手，止跌回穩帶動指數重返萬七，但終場還是沒能翻紅，下跌134.65點，收在17135.22點，雖然站穩萬七，但還是失守季線。分析師吳文彬指出，在外資賣超的情況下，內資會看的就是傳產股為主，特別是航運類股跟鋼鐵類股，以跌勢來講的話，(大盤)它也符合了黃金分割率，短線來講，吳文彬認為目前的季線，是多空的分水嶺，如果說大盤要轉強的話，必須先站穩季線。受亞股影響，外資賣內資接，站穩季線的話，應該會止跌了，盤面上電子傳產金融類股，全都應聲倒地，只剩百貨航運撐盤，航運漲幅更是來到2.54%，是近期新高，而航運三雄從高點回檔，已經連跌將近半個月，萬海28日開高震盪，尾盤急拉漲停，長榮早盤一度下探116元，收盤漲幅將近4%，陽明再度被列入注意，市場氛圍悲觀，三雄當中只有他收跌。吳文彬表示，萬一如果收盤又破季線的話，可能心態就要比較保守，今天的台積電萬海，已經出現表態，而且拉了241點的下引線，其實短線是應該要反彈。航運回穩拉下引線200多點，台積不續殺，投資人可以看，回彈做多，台股跌勢稍止，不過內外資會不會，同步轉賣為買，投資人也得好好觀察。\n\n\n\n\r\n                                新聞來源：華視新聞\r\n                            \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
        keywords=["台股", "股市"],
        category="財經",
        media="華視新聞",
        datetime="2021-07-28T18:47:00+08:00",
        link="https://news.cts.com.tw/cts/money/202107/202107282051061.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return cts.CTSNewsCrawler()


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
