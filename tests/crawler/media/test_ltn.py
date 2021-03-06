# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ltn
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
    name="自由時報電子報_1",
    link="https://news.ltn.com.tw/news/business/breakingnews/3604805",
    expected_output=NewsStruct(
        title="拼微解封商機   納智捷U6 GT藍調倍適版喊解封價72.8萬元",
        content="裕隆（2201）自主品牌納智捷搶先推出U6 GT藍調倍適版，解封價每輛72.8萬元，限量100輛。（圖由納智捷汽車提供）\n〔記者楊雅民／台北報導〕疫情降溫，三級警戒微解封，國人防疫自駕風潮可望掀起，裕隆（2201）自主品牌納智捷搶先推出U6 GT藍調倍適版，訴求「入門休旅的價格，旗艦休旅的車格」，解封價每輛72.8萬元，限量100輛。\n全新的「U6 GT藍調倍適版」全面強化運動配備，在中型旗艦SUV的大空間格局上打造出時尚、科技、質感的車室空間；類麂皮座椅以多層次紓壓材質強化左右支撐性、乘坐包覆感與止滑效果。\n後座6/4分離椅背設計，視情況可進行單邊放倒或全倒，更可使用後座椅左右兩側的One Touch快速翻折拉柄，一鍵翻倒，快速裝載大型物件；並配置後座出風口及智慧型電動尾門，可大幅增加空間應用的靈活度及舒適性。\n同時全面搭載12吋多功能 HD觸控螢幕、符合台灣特殊用車環境的AR View+行車AR影像系統，加上配置第10種視角Front View+無盲點車前影像、及安全實用的APA智駕輔助停車系統等多項先進配備。\n此外，同步搭載「開門防撞系統」，當後方有來車時，除了螢幕顯示紅框外，更增設「警示音提醒」；下車時「延長影像顯示時間5分鐘」或下車後車門上鎖自動關閉；亦可「設定熄火時，門鎖是否開啟」。\n納智捷表示，現在入主U6 GT智遊特仕版，本月限定解封價64.8萬元（原價74.8萬元），豪華的U6 GT藍調倍適版限量解封價72.8萬元（原價82.8萬元）。\n\n    一手掌握經濟脈動\n    點我訂閱自由財經Youtube頻道\n",
        keywords=["裕隆", "納智捷"],
        category="證券產業",
        media="自由時報電子報",
        datetime="2021-07-15T17:24:42+08:00",
        link="https://news.ltn.com.tw/news/business/breakingnews/3604805",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="自由財經_1",
    link="https://ec.ltn.com.tw/article/breakingnews/3468538",
    expected_output=NewsStruct(
        title="數位轉型成趨勢  叡揚訂閱制成穩定營收來源",
        content="\n叡揚資訊表示，在訂閱制與維護合約雙重助攻下，今年營收與獲利將持續穩健成長。左起為叡揚總經理陳世安、董事長張培鏞、發言人林秋丹。（記者陳炳宏攝）\n〔記者陳炳宏／台北報導〕資訊軟體商叡揚資訊（6752）今日表示，公司每年投入10%～12%的營收做為研發經費，發展對話機器人（Chatbot）、人工智慧（AI）等新關鍵技術，結合如智慧分文的自動公文系統等企業e化應用解決方案，在訂閱經濟商業模式助攻下，資訊軟體與服務訂單已明顯較過去成長，加上服務為訂閱制或簽維護合約，可逐月認列，今年營收與獲利有望逐步穩健成長，並突破去年雙位數成長幅度，對今年審慎樂觀。\n叡揚昨公告109年度財務報表，全年合併營收達10.91億元，首次突破10億元大關，年增12.75%、稅後純益達1.21億元，年增37.55%、每股稅後盈餘（EPS）為4.88元，營收、獲利、EPS皆創歷史新高。董事會決議每股配發2.2元現金股利及0.6元股票股利。\n叡揚表示，去年政府部門約佔營收的28%到29%，金融業佔38%、製造服務與醫療佔16%，今年成長動能，仍是自行開發的人資管理、知識管理、公文系統等軟體AI化，另外資安這幾年成長動能也很強。今年新成長動能，包括對話機器人（Chatbot）進入客戶應用系統，中小企業數位轉型雲端需求，以及新增加的醫院指標管理系統。\n叡揚董事長張培鏞表示，去年資訊服務業業績普遍不錯，主要是數位轉型為各產業發展趨勢，政府、金融、醫療產業、與中小企業，都會走向數位轉型，加上5G時代資安問題更被重視，今年營收有望延續這幾年年成長趨勢再望上提升。\n叡揚表示，目前經銷軟體業務佔營收30%，自行研發產品佔50%，客戶委外服務20%，此外，三家純網銀也都是叡揚客戶，去年開始逐步貢獻營收，今年朝向提供AI輔助加速核貸服務開發。\n\n    一手掌握經濟脈動\n    點我訂閱自由財經Youtube頻道\n",
        keywords=["叡揚"],
        category="證券產業",
        media="自由財經",
        datetime="2021-03-16T15:26:28+08:00",
        link="https://ec.ltn.com.tw/article/breakingnews/3468538",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ltn.LTNNewsCrawler()


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
