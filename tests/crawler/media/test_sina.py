# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import sina
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
    name="新浪新聞_1",
    link="https://news.sina.com.tw/article/20210318/37931108.html",
    expected_output=NewsStruct(
        title="營運創高＋高現金殖利率，IC通路至上、堡達、安馳「高而不貴」",
        content="\n 【財訊快報記者張家瑋報導】半導體族群陸續公布2020年財報與盈餘分配，IC通路商去年財報表現不僅令人驚豔，為近年來最佳成績，潛在高現金殖利率、低本益比更是值得重視，包括：至上( 8112 )、堡達( 3537 )、安馳( 3528 )現金殖利率均在6.4%至7%之間，相對於IC設計股王矽力-KY( 6415 )現金殖利率僅0.43%，IC通路族群真正凸顯「高而不貴」價值，具半導體產業高成長特性同時，又有高現金殖利率保本優勢。　　目前IC通路商已公布去年財報暨盈餘分派，業績高成長同時，又具備高現金殖利率潛在價值，現金股利最高者為崇越( 5434 )8元，其次為崇越電( 3388 )4.3元、至上3元、安馳2.9元、堡達2.5元。以今日開盤參考價計算，最高者為至上的現金殖利率7.04%、堡達6.84%、安馳6.42%、崇越6.25%，最低者茂綸( 6227 )也有5.07%。 　　對照於股后矽力去年業績續創新高，稅後純益32.78元，年增40.9%，每股稅後純益35.72元，IC通路去年受惠於疫情帶動宅經濟需求，業績表現絲毫不遜色，崇越去年稅後純益20.68億元，年增20.09%，每股稅後純益11.38元，營收、獲利雙雙創高，而至上、安馳每股稅後純益分別在4.22、3.18元也創下新高，同樣展現半導體產業高成特性。 　　法人指出，當大盤振幅劇烈時，高現金殖利率、低本益比、配發率穩定加上營收成長的個股普遍受到法人買盤青睞，股價短線回測也具備下檔支撐；當大盤止跌回穩時，高現金殖利率股仍擁有籌碼面的優勢，資金湧入助漲個股的空間更大。 　　目前尚未公布盈餘分派包括：增你強( 3028 )、大聯大( 3702 )、文曄( 3036 )、敦吉( 2459 )、華立( 3010 )等，去年業績均表現不俗，維持過去高現金殖利率配發，相當值得期待。今年業績展望，至上今年持續受惠中國手機品牌市占率重新洗牌，OPPO、小米、Vivo、榮耀、傳音等搶食商機，帶動至上記憶體拉貨動能強勁。安馳則因下游客戶積極建立安全庫存水位，今年兩大產品線均推出新款高階整合方案，並開發國防、車載及醫療等利基型的高階整合方案，整體營運可望維持穩健成長動能。 \n",
        keywords=["財訊快報", "財經", "新浪新聞中心"],
        category="新浪新聞中心_財經",
        media="新浪新聞",
        datetime="2021-03-18T12:10:09+08:00",
        link="https://news.sina.com.tw/article/20210318/37931108.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="新浪新聞_2",
    link="https://news.sina.com.tw/article/20210415/38230928.html",
    expected_output=NewsStruct(
        title="建通國際高雄港S19號碼頭動土典禮  獲指定為煤炭船優先靠泊的環保碼頭",
        content="\n     【焦點傳媒社/總社長孫崇文報導】    建通國際股份有限公司於高雄港洲際二期S19號碼頭，今(15)日舉辦開工動土典禮，為因應環保趨勢，配合臺灣國際商港長期規劃，及提高裝卸作業效率，以縮短船舶在港時間，增加貨主商業流通之彈性，進一步提升高雄港競爭力，建新國際(8367)攜手台通光電(8011)、環臺國際及安順裝卸成立建通國際股份有限公司，針對逸散性貨物帶來台中港安順裝卸104號專用碼頭的成功經驗，共同打造高雄港第一座「不落地、不揚塵、密閉式」的低汙染高效率碼頭。   燃煤自古即為民生經濟之重要基石，具有價格低廉，來源分散且供應無虞的優點，時至今日仍深受仰賴。   按國際能源總署(IEA)2018年所發布之預測，至2040年全球將持續維持0.1%年成長率，期盼在政府環境保護政策全方位、標準化的有效控管下，可以兼顧民生經濟及生活品質的需求，讓人民吃得飽又活得好。   順應大勢所趨，建通國際積極建設S19號碼頭，獲指定為煤炭船優先靠泊的環保碼頭，且具備承做熟白料貨物之彈性。興建計畫斥資14億元，並取得經濟部「中小企業加速投資行動方案」審查通過的肯定，布置包含兩座密閉式煤倉、三部自動化專利卸煤機、成熟的輸送帶設備，及智慧化即時監控系統，軟硬體兼備，以實現重環保、高效率、智慧化的核心目標，提供更友善環境且便捷的煤炭儲轉服務，預計於2022年第四季投入營運，期盼帶來一股新氣象，為環境、航港、貨主及股東創造多贏局面。   延伸閱讀：【焦點傳媒社】            \n\t\t\t    ",
        keywords=["焦點傳媒社", "社會", "新浪新聞中心"],
        category="新浪新聞中心_社會",
        media="新浪新聞",
        datetime="2021-04-15T14:04:38+08:00",
        link="https://news.sina.com.tw/article/20210415/38230928.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return sina.SINANewsCrawler()


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
