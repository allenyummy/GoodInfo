# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import setn
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
    name="三立新聞_1",
    link="https://www.setn.com/News.aspx?NewsID=981898",
    expected_output=NewsStruct(
        title="陽明大戶怒賣25筆104！網全笑翻",
        content="\n\n財經中心／戴玉翔報導台股連7殺！不管是電子股還是航運股都進行修正。而貨櫃三雄中的陽明（2609）第2季獲利飆出逾1個股本，可惜股價表現未能反映利多，終盤更是以下跌作收。就有眼尖的投資人發現在今日11時30分左右，陽明成交連續25筆賣單都掛104張，有網友幫忙翻譯出大戶的心聲，引起熱烈討論。▲陽明Q2賺超過1股本，上半年EPS 17.88元。（圖／陽明海運提供）今日11時30分，陽明一口氣出現25筆委賣，每一筆交易張數都是104張，成交價約135元。就有網友笑稱應該是有大戶不爽陽明未能反映利多，一怒之下大量拋貨。▲今日11時30分，陽明一口氣出現25筆委賣，每一筆交易張數都是104張，成交價約135元。（圖／讀者提供）有網友幫忙翻譯出大戶的心聲，有一派網友認為「104」可能是取自「104人力銀行」，也就是賠錢賠到該找工作了，也有另外一派網友認為「104」若是以「E04」的中文輸入法，就是大戶的心聲了。其他網友們也紛紛回應，「找工作囉」、「E04 自己看鍵盤」、「是下看104元」、「叫少年股神好好找工作」、「不就奉勸套牢水鬼回去工作嗎，別做航運翻身夢」、「玩不贏大戶」、「主力叫你回去工作」。瞭解更多>>全球航運大漲！「貨櫃三雄」股價腰斬下一步？謝金河給解答https://www.setn.com/News.aspx?NewsID=981797台股鬼月驚人巧合！鬼門開「9跌1漲」　專家曝恐跌到這時https://www.setn.com/News.aspx?NewsID=980693★ 三立新聞網提醒您：內容僅供參考，投資人於決策時應審慎評估風險，並就投資結果自行負責。\n\n",
        keywords=["大戶", "陽明", "104人力銀行", "股本"],
        category="財經",
        media="三立新聞",
        datetime="2021-08-13T14:46:00+00:00",
        link="https://www.setn.com/News.aspx?NewsID=981898",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="三立新聞_2",
    link="https://www.setn.com/News.aspx?NewsID=983646",
    expected_output=NewsStruct(
        title="他驚爆：中國若攻台　美國將扶植建國",
        content="\n\n政治中心／台北報導阿富汗政權更迭，自由台灣黨創黨主席蔡丁貴認為，當中國侵略台灣的時候，中華民國流亡政府會再度落跑或直接投降；台灣人民不會落跑，美國政府也不會落跑，會讓台灣脫胎換骨轉型成一個新而獨立的主權國。▲蔡丁貴認為，中國若攻台，美國將扶植台獨建國。（圖／記者盧梅攝）蔡丁貴昨（16日）在臉書發文說，阿富汗政府快速垮台，可觀察美國國際外交政策的運作，美國政府是國際大國，可以算是老大哥，以前的蘇聯及現在的中國都有企圖跟他爭鋒，還沒有成功。為了維持老大哥的形象與責任，美國與其他國家的外交政策似乎有些規則可以觀察。他表示，美國政府與台灣人民的非正式外交關係是美國國際外交政策運作成功的標竿。美國支持過中華民國政府、支持過南越政府、支持過菲律賓馬可仕政權、支持埃及穆巴拉克政權、也支持現在垮台的阿富汗政府，結果美國支持的政府或政權都被對手推翻下台。他認為，美國現在也支持中國習近平政權，雖然美中角力也正在激烈進行中。原因無他，美國支持過的這些政府（權）都是背棄當地人民而貪污腐化的政府。即使美國耗盡洪荒之力的資源，這些背離當地人民的腐化政府（權）最後還是倒台。蔡丁貴表示，美國政府的國際外交政策最不相同的特殊案件，卻是以「非正式」外交關係支持台灣人民（不是支持現在的中華民國流亡政府），讓台灣人民有空間與中華民國殭屍流亡政府的鬥爭逐步突破，逼使中華民國殭屍流亡政府慢慢解構，開放自由民主的空間。雖然還沒有完全到位，卻是為美國政府建立一個「支持當地人民」就是外交政策運作成功的指標範例，正式或非正式外交關係都沒有關係。他說，當中國共產黨打敗了美國支持的中國國民黨，美國最後還是與中國共產黨重修舊好，越南的例子也是如此，可以預料多年之後美國也會與新的阿富汗政府建立新的外交關係。這些外交關係會不會順利成功，就看美國的外交政策運作是否符合當地人民的需求？還是只是討好當地政府對人民的控制？蔡丁貴表示，當中國侵略台灣的時候，中華民國會再度落跑或直接投降。不過，台灣人民不會落跑，美國政府也不會跟著中華民國流亡政府落跑，美國政府將會跟著台灣人民守住台灣的自由與民主。然後就是建立「法治（rule of law)」的體制。台灣人民就會脫胎換骨轉型成立一個新而獨立的主權國。歡迎中華民國流亡政府再度流亡離開台灣，讓「中華民國台灣」只剩下「台灣」。\n\n",
        keywords=["美國", "阿富汗", "台獨", "蔡丁貴"],
        category="政治",
        media="三立新聞",
        datetime="2021-08-17T10:58:00+00:00",
        link="https://www.setn.com/News.aspx?NewsID=983646",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return setn.SETNNewsCrawler()


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
