# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import bcc
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
    name="中國廣播公司_1",
    link="https://www.bcc.com.tw/newsView.6473942",
    expected_output=NewsStruct(
        title="「這家超商」6/23開賣快篩試劑　雙北2門市限量100盒",
        content="\r\n                        為了方便民眾居家檢測新冠肺炎，食藥署在19日公布核准5款家用快篩試劑，可就近到藥局、醫療器材販售業者，如藥妝店、醫療器材行、便利商店等商家選購。萊爾富位於雙北的2家門市明(23)日起將首度開賣家用快篩試劑，每店限量100盒，售完為止。萊爾富首度引進國產泰博科技的「福爾威創家用新型冠狀病毒抗原快速檢驗套組」，明天下午3點起，將在台北市迪化店、北縣五工店限量開賣，每盒5入售價1700元，每店限量100盒，不拆售。根據食藥署公布的指引，如果快篩陽性，居家檢疫或隔離者須先與衛生單位聯繫，一般民眾則到社區採檢院所採檢確認；如果是陰性，民眾仍要遵循防疫規範，做好個人防護，持續自我健康管理。(快篩試劑資料照）\r\n                    ",
        keywords=None,
        category=None,
        media="中國廣播公司",
        datetime="2021/06/22 18:49 報導",
        link="https://www.bcc.com.tw/newsView.6473942",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="中國廣播公司_2",
    link="https://www.bcc.com.tw/newsView.4839712",
    expected_output=NewsStruct(
        title="台積電衝關未成　聯電ADR爆漲股價再登新高",
        content="\r\n                        半導體類股正當紅，台積電今天（24日）早盤衝關500元短暫達標後拉回，聯電延續昨天的強勢，在ADR飆漲超過20%助威下，股價漲幅超過7%，最高攻至39.7元，市值擠下股王大立光，繼續成為台股人氣王。因為聯電的狂飆，大盤儘管稍事休息，拉回的幅度也很有限。（張佳琪報導）台股週一的兩大支柱台積電、聯電，週二股價兩樣情，台積電挑戰500元大關，早盤開盤隨即攻頂，但是衝高後買盤追價謹慎，導致股價翻黑呈現小跌。聯電因週一股價漲停板鎖住，美國ADR強漲20.24%，帶動股價開盤後強勢走高，隨即衝過39元一路向上，攻至39.7元，股價又改寫18年新高，且追價買單積極，漲幅超過7%，市值擠下股王大立光。讓股價瞬間點火爆衝的關鍵是美系外資分析師最新出具的報告大力看好聯電。理由是受惠於5G、AI、高速運算等發展，聯電產用率將提高至90%到95%，因此，8吋晶圓價格調漲、12吋晶圓產用率提升，以及28奈米拓展有成，推估聯電明後年資本支出將達12億美元，重申「買進」評等，目標價由32元上調至54.5元。分析師表示，三大法人週一同步大買聯電，週二的漲勢，內外資應都有貢獻。至於是否漲到外資報告訂下的目標價，分析師認為，以今年聯電EPS預估2.25元推算，如果漲到54.5元，本益比落在24倍，雖然高但不至於離譜，因此認為如果外資買盤力道夠強，目標價就可能達標。（圖：雅虎奇摩）\r\n                    ",
        keywords=None,
        category=None,
        media="中國廣播公司",
        datetime="2020/11/24 11:26 報導",
        link="https://www.bcc.com.tw/newsView.4839712",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return bcc.BCCNewsCrawler()


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
