# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import moneyudn
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
    name="經濟日報_1",
    link="https://money.udn.com/money/story/5607/5047950",
    expected_output=NewsStruct(
        title="盤點12月必漲好股 精選8檔年底最強候選黑馬",
        content="進入到12月份的台股是否還可以繼續漲下去呢？更重要的是，哪些個股能在12月脫穎而出？專家統計了過去10年12月份上漲機率100%的個股，幫投資人找出意想不到的12月強股。\n\n\n\r\n台股自2020年3月份的低點8523點起漲迄今，已經滿足了黃金比率的1.618倍，換算起來過去8個月的時間漲了超過5000點，可說是月月漲、季季高，尤其是在11月的美國總統大選之後，在強勢新台幣的帶動下，台股上漲超過1000點，整體來看，這波多頭的走勢銳不可當，也讓投資人賺得荷包滿滿！\n\n\n\n歷年12月上漲機率高\n\n\n\r\n然而，進入到12月份的台股是否還可以繼續漲下去呢？我們先從加權指數歷年來12月份的漲幅來看，統計過去10年僅有2018年12月份是下跌的，其餘都是上漲。以過去10年的資料來看，台股12月份上漲機率高達90%，如果統計過去20年的資料，總共有4次是下跌，16次上漲。以過去20年來看，台股12月份上漲的機率也有80%。就台股歷年統計資料分析，12月份上漲的機率算是滿高的，那麼，我們就來看看有哪些是12月份上漲機率較高的個股。\n\nfacebook\n\r\n統計過去10年12月份上漲機率100%的個股，包括：水泥類股的東泥（1110），有鑑於全球熱錢流竄，股市呈現多頭走勢，再加上廠商紛紛加碼投資建廠與建築所需的相關需求，東泥9月與10月營收呈現年增與月增同步增長的情況，近期成交量也有逐步放大的跡象，但是仍是屬於交易量較小的股票，所以在買進的時候不宜買進太多張數，不然有可能會出現「價格被自己買上去，等到12月底要賣出的時候，價格又被自己賣下來」的情況。\n\r\n南亞（1303）可說是交易量大且占大盤權重高的股票，所以頗受外資法人的青睞，雖說投信是站在賣方，但是以南亞身為台灣50成分股的角度來看，仍是以外資的買盤為主要觀察指標。\n\r\n從外資籌碼來看，近期外資買超南亞已經持續將近1個月的時間了，看起來外資相對看好南亞在年底時的表現，主要是因為看好客戶端需求回溫、積極備貨，使得相關產品的價格走揚，進而推升公司營運成長動能。\n\n\n\n南亞等待低點再布局\n\n\n\r\n就操作面來說，過去10年南亞12月的平均漲幅約為5%，如果以過去3年的12月平均漲幅來看，約在1.6%左右，所以投資人可以留意南亞是否有因為台股漲多壓回而導致的低點出現，再做適量的布局即可，畢竟要買低才有賣高的機會。\n\r\n聯發（1459）主要從事聚酯加工絲的製造，也是一檔交易量較小的股票，因此投資人在買進的時候不要太大量去買進，避免因為成交量較小而致使買賣價差變大，進而產生買進、賣出時的虧損。\n\n\n\n\n\r\n【完整內容請見《非凡商業周刊》2020/11/27 No.1225】想了解更多，詳洽02-27660800 當沖比直逼4成的台股，你心動嗎？當沖就像捕魚，不見得天天可沖，掌握訣竅才能輕鬆捕魚，即日起只要訂閱非凡商業周刊，就送你《當沖聖經別冊》，數量有限，先訂先贏。《2021世紀大轉折》把握百年難得一遇的財富重分配機會，狂銷熱賣中，想了解更多資訊，請上「非凡優購」網站\n\n\n\nfacebook",
        keywords=["台股", "南亞", "投資", "外資", "營收"],
        category="證券",
        media="經濟日報",
        datetime="2020-11-27T12:55:38+08:00",
        link="https://money.udn.com/money/story/5607/5047950",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="經濟日報_2",
    link="https://money.udn.com/money/story/5612/5560454",
    expected_output=NewsStruct(
        title="飲料廠熱戰 新品搶市",
        content="即將邁入7月酷暑，飲料大戰趨於白熱化，根據統計台灣飲料市場去年產值近580億元，且近兩年皆有成長。今年即使有疫情變數，味全（1201）、黑松、泰山等大廠依然出招搶商機，推新品搶灘，期望衝出好成績。\n\n\n\r\n今年飲品推出方向還是以獨特和健康為主軸，氣泡飲、果汁、咖啡是主打產品，酸甜口味在夏季最受消費者青睞。\n\n\n\r\n根據經濟部統計處資料顯示，台灣去年碳酸飲料銷售額達53.8億元，年增6.24%，為近五年內新高。黑松表示，看好消費者對氣泡飲品需求激增，旗下黑松C&C今年首次與日本軟糖品牌「Puré」聯名，將葡萄軟糖口味轉為氣泡飲，於全家獨家販售。\n\n\n\r\n黑松長銷咖啡品牌「韋恩」去年推出瓶裝咖啡搶市，帶動韋恩咖啡去年整體業績成長15%以上，今年找來四大極地超馬總冠軍陳彥博擔任代言人，期望再衝出雙位數成長。\n\n\n\r\n泰山旗下為氣泡水市占第一名的Cheers，今年首度發展全新「Cheers+」系列。泰山表示，有消費者不愛喝甜汽水，但也不習慣無糖氣泡水，為增加飲用動機，推出Cheers+首支新品果醋氣泡飲搶市，有望持續帶動氣泡水類產品營收。\n\n\n\r\n今年泰山攜手兩大餐飲品牌推出代工飲品，頻頻在7-ELEVEN亮相，搶飲料商機，包括港點添好運的楊枝甘露、以及統一超轉投資餐廳「21PLUS」店內熱銷飲品冬瓜檸檬凍飲，也都有不錯銷售。\n\n\n\r\n味全長銷的冷藏咖啡品牌「貝納頌」，為迎戰罐裝咖啡市場，搶攻70億元包裝咖啡市場，今年首度推出大容量的瓶裝咖啡「貝納頌極品大咖啡」。近期因應疫情所需，該產品更上架至各電商平台，搶居家上班商機。\n\n\n\r\n味全表示，果汁品牌每日C，今年暑期預估有望成長20%；農搾果汁系列有望成長15%。",
        keywords=["泰山", "黑松", "果汁"],
        category="產業",
        media="經濟日報",
        datetime="2021-06-27T01:00:24+08:00",
        link="https://money.udn.com/money/story/5612/5560454",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return moneyudn.MoneyUDNNewsCrawler()


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
