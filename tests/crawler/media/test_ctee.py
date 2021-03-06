# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ctee
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
    name="工商時報_1",
    link="https://ctee.com.tw/news/stocks/491412.html",
    expected_output=NewsStruct(
        title="7/21盤前掃描》300億上膛 萬海再擴船隊",
        content="萬海表示，全球缺船、缺櫃潮帶動船舶與貨櫃租金飆漲，對經營成本造成壓力，據調查船舶租金近一年來大漲三～四倍。萬海因應內租船租金提高、租期跟著增加，船舶調度以及起、解租需求增加…閱讀全文\n受樂觀財報鼓舞，投資人對經濟復甦的看法恢復樂觀，投資人逢低買進，美股大洗三溫暖，19日（周一）大暴跌的三大指數， 20日（周二）全數強勁反彈， 平均漲幅均逾1.5%…閱讀全文\n台積電股價在法說會後下挫，花旗環球證券台灣區研究部主管徐振志指出，第二季財報不如預期、第三季毛利率展望差強人意，是引動殺盤主因，不過，市場開始修正之前過高的期望值…閱讀全文\n高端（6547）研發的新冠肺炎國產疫苗，通過台灣緊急使用授權（EUA），未來不僅有機會進軍國際打世界盃，也將在國內建置完整疫苗產業供應鏈…閱讀全文\n台股20日收盤重挫260.51點，收在17528.74點，航海王紛紛落難，貨櫃三雄長榮、陽明、萬海股價一度逼近跌停，都說本周是超級航運周，航運景氣好到不行，股價怎麼會這麼不給力？分析師指出，航運股的基本面的確非常好，但…閱讀全文\n受美股重挫影響，台股20日開盤即跌破月線，盤中更一度重挫近300點，終場下跌260點，三大法人全數站賣方，合計大賣357.9億元，所幸盤面仍有包括欣銓（3264）、通嘉（3588）等14檔逆風表現、價量俱揚...閱讀全文\n台股周二重挫260點，收在17,528點，其中航運再度淪為空襲箭靶，貨櫃三雄跌幅8、9%以上逼近跌停，不少手中有船票的散戶相當驚慌，急問航運股是不是沒救了。法人指出…閱讀全文\n\n🎯工商時報IG新登場！搶先 [樂·讀] https://www.instagram.com/ctee.ig/🎯加入工商時報Telegram頻道  https://t.me/ctee_telegram🎯微股力達人-工商時報加關注 📱精選新聞不漏接!  ",
        keywords=["台股", "盤前掃描"],
        category=None,
        media="工商時報",
        datetime="2021-07-21",
        link="https://ctee.com.tw/news/stocks/491412.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="工商時報_2",
    link="https://ctee.com.tw/news/stocks/487126.html",
    expected_output=NewsStruct(
        title="恩德福裕喬福 訂單旺到Q4",
        content="恩德（1528）、喬福（1540）、福裕（4513）三家工具機廠接單持續好轉，訂單能見度至少看到第四季，首季已全數轉虧為盈，全年拚營收成長，獲利轉正。\n恩德工具機及木工機年底前訂單滿載，木工機開始接明年訂單，恩德董事長廖文嘉表示，明年斥資至少5億元，在苗栗投資擴建工具機廠。\n台灣工具機廠去年只有亞崴（1530）、程泰（1583）、瀧澤科（6609）等少數工具機廠獲利，恩德、喬福、福裕等出現虧損，三家工具機廠今年第一季陸續接獲大陸或歐洲訂單，今年首季全數轉虧為盈，目前在手訂單至少三～四個月，部分大型機台在手訂單長達半年以上，訂單能見度看到第四季。\n福裕持續接獲大陸及台灣汽車相關產業訂單，第一季轉虧為盈，EPS為0.1元，目前在手訂單3億多元，訂單能見度看到第四季，今年訂出營收成長，獲利轉正的營運目標。\n福裕董事長張寶銘表示，看好電動車及半導體等產業未來發展前景，正積極布局。福裕針對電動車產業，鎖定電動車鋰電池零件及鋰電池托架等相關廠商；至於半導體產業使用鋁碳新材料取代鋁、鎂等材料製品，開發應用在鋁碳新材料零件加工機台，搶攻半導體產業訂單。\n喬福指出，最近持續接獲訂單，其中代理商接獲長達18米的大型龍門訂單，預計第四季出貨，目前在手訂單2億多元，訂單能見度看到第四季，目前產能還可以接新訂單。\n恩德今年第一季因新台幣匯率升值，認列匯損0.17億元，第二季認列匯損可望收斂。恩德德國廠生產的工具機主要供貨給德國當地、奧地利及瑞士等國家，目前工具機接單看到年底，產能滿載，恩德木工機出貨至北美等國家採FOB報價，運費由客戶負擔，較不受運費飆漲影響。\n恩德木工機年底前訂單全滿載，開始接明年訂單，現在手訂單13億元，今年營收預估比去年微幅成長，今年營運著重在稅後利潤轉正，目標是獲利要大幅成長。\n廖文嘉指出，恩德基於工具機廠產能滿載，打算在台灣擴建第二生產基地，目前規劃在苗栗建廠，預計明年初動工，明年底完工，主要生產高階大型五軸機，連同土地、土建及機器設備，資本支出至少5億元。",
        keywords=["訂單", "恩德", "喬福", "福裕"],
        category=None,
        media="工商時報",
        datetime="2021-07-12",
        link="https://ctee.com.tw/news/stocks/487126.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ctee.CTEENewsCrawler()


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
