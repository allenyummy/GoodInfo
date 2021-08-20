# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import newtalk
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
    name="新頭殼_1",
    link="https://newtalk.tw/news/view/2021-08-13/620248",
    expected_output=NewsStruct(
        title="「記憶體寒冬將至」 美光科技重挫6%",
        content="美光科技 (Micron Technology) 公司近期接連遭受打擊，12日重挫6.37%，收報70.25美元，本週四個交易日內重挫15%，創下去年5月以來最差單週表現，今年累計下挫5.13%，遠遠跑輸今年上漲14.96%的納指和費城半導體指數的18%漲幅，近期的表現更與不斷創新高價的標普指數和道指嚴重脫節。\n美光科技12日大跌的引爆點是摩根士丹利發布名為「記憶體寒冬將至」的產業報告，將美光的評級由「加碼」降為「持平」，反映美光的主力產品 DRAM 記憶體市況下滑的擔憂，明年有很高的跌價風險，並將該股目標價由105美元降為75美元。\n記憶體情報權威機構集邦科技 (TrendForce) 預測，DRAM 今年第四季的合約價將下挫5%，主因是個人電腦製造商目前手上的 DRAM 庫存過多，這些下游製造商先前擔心半導體缺貨而大量囤積 DRAM 產品。但現在歐美地區逐漸解封，隨著民眾逐漸恢復正常生活，對筆電的需求已開始下降，進而削弱 PC DRAM 的總需求量。\n美光遭受的重挫對半導體族群產生負面漣漪效應，威騰電子 (Western Digital) 下挫6.5%，科磊（KLA-Tencor）和泛林集團 (Lam Research) 也下跌4.1%，並拖累費城半導體指數下挫1.13%。",
        keywords=["美光科技", "記憶體", "DRAM"],
        category="國際",
        media="新頭殼",
        datetime="2021-08-13T15:41:22+08:00",
        link="https://newtalk.tw/news/view/2021-08-13/620248",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="新頭殼_2",
    link="https://newtalk.tw/news/view/2021-08-11/619072",
    expected_output=NewsStruct(
        title="貨櫃三雄股價僅16個月飆漲30倍！ 但「股市非常態波動也是殺人陷阱」 專家說後市該這樣看",
        content="遍閱台股歷史，資本額達2百餘億元到近5百億元的重磅股族群，可以在短短16個月，橫空創造出30倍左右的漲幅者，只有去年爆發疫情以來的陽明、長榮及萬海三家貨櫃航運股。這種絕無僅有，未知是否絕後，卻肯定是空前的紀錄，2、3年後股價又會是什麼景況？相信是未來商學院個案研究必選的案例。\n毛澤東有一句名言：天下大亂，形勢大好。身為圖謀「主角換人做看看」的奪權者，短短8個字精簡扼要地點出了3千年中國歷史未曾撼動過的鐵律：改朝換代的必要條件，就是天下大亂。\n想不到這句話，恰恰可套用在疫情以來的貨櫃航運股。如果不是疫情導致全球的經濟活動作息大亂，陸、海運輸能力近乎半癱瘓，怎麼可能出現貨櫃航運商漫天喊價，託運客戶卻不能就地還錢的情境？\n台灣全部航運股的經濟產值不到電子股的10分之1，今年以來的台股，卻屢屢出現航運股成交值大於電子股的現象，這不也是一種主角換人做看看的架勢？台股就此改朝換代，由航運股掌權主導嗎？\n非常態波動 最誘人的陷阱\n中國式史觀有這麼一說：可以馬上得天下，不可以馬上治天下。大意是說，得天下通常耗時不長，是一個朝代過渡到另一個朝代的非常態。治天下則是動輒2、3百年以上的國祚，是一種新常態。換句話說，短期得天下的非常態，不等同於長期治天下的新常態。\n現階段貨櫃航運股的超高獲利，絕對是一種非常態，未來的命運青紅燈，就看能否非常態轉化成新常態（持續維持高獲利）。此時的股價已是騎虎難下，若轉化成功，3、4百元都有可能；若回歸舊常態（過去20年獲利乏善可陳），兩三年後的低點，先看今年天價打兩折\n股市的非常態波動是最誘人的暴利機會，卻也是最可怕的殺人陷阱。上個世紀美國一位績效卓著的基金經理人，有一句簡短卻令人折服的名言：「Get rich with the glitch.」Glitch的意思大約是故障、失靈，引申在金融市場，就是市場正常的定價機制失靈，出現大漲大跌的非常態波動。\n非常態波動肇因於人性基本上短視近利，貪婪與恐懼情緒主導下的市場行為，急切衝動，再加上群體的相互抱團取暖心態，新聞不斷地刺激強化作用，以及有心人的渲染擴散，無識者的搖旗吶喊助陣，很快就形成市場的群體暴動。此時只有極少數人思考常態、非常態或新常態這些未來課題，市場也只能反映當下的供需變化而大漲或大跌。\n激昂的群眾情緒，終將隨著事實證據的呈現而轉趨平靜。非常態的大漲大跌，終將面臨進入新常態或回歸舊常態的考驗。暴漲後的案例，有9成以上是回歸舊常態，也就是跌回非常態波動發生前的常軌，只有極少數能轉化為新常態，穩於高檔或更上一層樓。\n暴跌後的案例，如果是發生在股市整體評價，也就是指數，除了百年一遇的大蕭條，幾乎全數可在2、3年內回歸舊常態，且建立出新的上漲模式。所以大跌後買指數型ETF，中期幾乎穩賺不賠且投報率很可觀。\n股價非常態性暴漲後，要說服市場高股價是新常態非常困難，即使市場「暫時買帳」，也會有一段「留校察看」時期。特斯拉就是一個例子，去年暴漲後回檔，迄今距離歷史新高仍有25％左右差距。基本面已確定電動車是未來的新常態，特斯拉雖然是先發者，市場還是要看競爭力、營收及獲利成長等再重新定價。\n台積電亦然，去年疫情以來10個月漲幅近兩倍，以台積電的屬性，已略顯現非常態。半導體晶片是全球未來不可或缺的戰略產業，台積電堪稱是未來新常態的要角，股價仍須在大漲後，接受市場的質疑。\n(本文經《今周刊》同意轉載，更多資訊詳見《今周刊》第1286期)。",
        keywords=["貨櫃航運股", "台股", "疫情", "特斯拉"],
        category="財經",
        media="新頭殼",
        datetime="2021-08-11T15:22:51+08:00",
        link="https://newtalk.tw/news/view/2021-08-11/619072",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return newtalk.NewTalkNewsCrawler()


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
