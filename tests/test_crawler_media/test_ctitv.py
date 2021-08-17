# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ctitv
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
    name="中天新聞_1",
    link="https://gotv.ctitv.com.tw/2021/08/1855737.htm",
    expected_output=NewsStruct(
        title="申請Delta病毒株「測試再闖關」！聯亞EUA沒過&#8230;將提申訴　已規劃在印度進行第3期臨床",
        content="記者黃心瑀／綜合報導\n衛福部長陳時中昨 （16） 在記者會上遺憾的表示，聯亞疫苗UB-612 EUA審核沒有通過。對此，聯亞於晚間發聲明表示，食藥署所公告的中和抗體力價測試當中，是以原始新冠肺炎株當作標準，會再申請以Delta病毒株進行測試。\n 衛福部食藥署長吳秀梅表示，聯亞EUA審查會議於15日召開，一共有20名專家出席，議中比較聯亞疫苗的中和抗體數據，以及國人接種AZ外部對照組的中和抗體數據，發現未能達到2項國產疫苗EUA療效評估標準；會議結果為，4人補件再議，有17人表示不通過，因此建議不予核准專案製造。\n對此，聯亞表示，對於EUA審核未通過一事，將會向藥品查驗中心（CDE）及食藥署 （TFDA） 提出申訴，更提出食藥署所公告的中和抗體力價，是以原始新冠肺炎病毒株作為標準，將會申請以Delta病毒株做測試，再申請重新判定審查結果。\n聯亞說，目前已經收取政府50%的訂金，投入生產疫苗成本之中，不可退還，目前國內的二期試驗將繼續進行，並對第三期臨床效益進行重新評估，公司也規畫將在印度展開第三期臨床試驗。\n⭐️中天唯一指定電商平台，支持中天就來快點購，多樣精選商品等你快點購！⭐️認同中天理念請支持中天文創，馬克杯、帆布袋、T恤等商品陸續推出，快來快點購！",
        keywords=["Delta", "聯亞"],
        category=None,
        media="中天新聞",
        datetime="2021-08-17T09:55:38+08:00",
        link="https://gotv.ctitv.com.tw/2021/08/1855737.htm",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="中天新聞_2",
    link="https://gotv.ctitv.com.tw/2021/08/1855470.htm",
    expected_output=NewsStruct(
        title="快訊／仁寶捐1億元給慈濟！跟進台積電、鴻海、台泥「支援疫苗採購」　",
        content="記者許元馨／綜合報導\n慈濟基金會已簽訂BNT原廠疫苗採購合約，疫苗將全數捐贈給政府給民眾施打，代工廠仁寶今（15）日宣布將1億元給慈濟基金會，幫助疫苗採購案。\n仁寶為了實踐社會公益，宣布捐贈1億元給慈濟基金會，協助疫苗採購，希望台灣能盡早戰勝疫情。 而仁寶是繼台積電、鴻海之後，另家科技廠出手捐贈採購疫苗。 \n此外，針對慈濟慈善基金會於7月21日，簽訂購買500萬劑BNT疫苗，並全數捐贈給政府主管機關，台泥在12日的董事會中做出決議，將參與這樣捐贈計畫，資助1億元給慈濟做為購買疫苗使用。 \n【延伸閱讀】快訊／傳BNT「9月中」抵台！陳時中鬆口回應了\n⭐️全能蜂膠濃萃膠囊，嚴選原料和專業技術，提供日常所需營養，溫和調節生理機能。\n ⭐️來自菊島的尊榮味蕾饗宴，極致口感、鮮甜海味，秘製獨家配方、澎湖福朋喜來登，五星嚴選頂級海皇干貝XO醬。",
        keywords=["1億元", "仁寶", "慈濟", "捐贈"],
        category=None,
        media="中天新聞",
        datetime="2021-08-16T18:35:16+08:00",
        link="https://gotv.ctitv.com.tw/2021/08/1855470.htm",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ctitv.CTITVNewsCrawler()


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
