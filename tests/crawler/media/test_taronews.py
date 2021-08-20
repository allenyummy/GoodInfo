# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import taronews
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
    name="芋傳媒_1",
    link="https://taronews.tw/2021/08/17/771295",
    expected_output=NewsStruct(
        title="當沖降稅延長有望  國發會本週找財金2部會交換意見",
        content="\n\n當沖降稅是否延長，成為近期市場熱議話題，國發會將邀金管會、財政部開會討論，本週初步交換意見；知情官員表示，目前還是往延長的方向討論，只是降稅年限可能取折衷值。\n當沖證交稅稅率減半優惠將於年底到期，金管會今年2月下旬向財政部建議再延長5年，不過傳出財政部並未放棄取消優惠，或是傾向縮短降稅優惠年限。\n行政院政務委員、國發會主委龔明鑫近期將邀金管會、財政部共同討論；凝聚共識後，財政部將送法案至行政院審查，院會拍板後，再送入立法院、啟動修法。\n知情官員表示，基本上會往延長的方向討論，只是比例的問題，畢竟財政部、金管會考量因素不同，延長時間點可能需要再協商，找出雙方可接受的方案。\n財政部官員認為，經過4年多，台股重返榮景，交易量也擴大不少，此時是否還是只能單靠稅制工具來救市，有沒有非稅制的工具可發揮替代效果，可以再思考。另外，站在租稅公平立場一定要檢討，才不違背納稅者權利保護法、財政紀律法的立法意旨，租稅優惠不得過度，也應有適當期限。\n金管會官員則說，金管會先前已提出當沖證交稅稅率減半優惠措施延長5年建議，後續基於協助立場，持續提供財政部所需資料作參考，財政部為稅制主管機關，會通盤考量。\n（新聞資料來源 : 中央社）\n",
        keywords=["金管會", "國發會", "財政部", "稅制", "龔明鑫", "納稅者權利保護法", "稅率", "證交稅"],
        category="財經",
        media="芋傳媒",
        datetime="2021-08-17",
        link="https://taronews.tw/2021/08/17/771295",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="芋傳媒_2",
    link="https://taronews.tw/2021/08/17/771237",
    expected_output=NewsStruct(
        title="阿富汗前車之鑑？蘇貞昌：有些人老長敵人威風",
        content="\n\n中廣董事長趙少康質疑阿富汗是台灣前車之鑑，行政院長蘇貞昌今天表示，他們在戒嚴中不怕被殺被關，打開民主大門，今天有強國說要併吞台灣，他們一定守護這個國家，不像有些人，老是長敵人威風，減自己志氣。\n蘇貞昌上午在嘉義縣長翁章梁、立委蔡易餘的陪同下，視察嘉義蒜頭糖鐵延伸計畫，會前接受媒體聯訪。\n阿富汗情勢轉變，總統甘尼（ Ashraf Ghani ）選擇遠走他國。中廣董事長趙少康質疑，未來若台灣也面臨他國兵臨城下，總統蔡英文與行政院長蘇貞昌是否也會做出同樣選擇。\n蘇貞昌表示，當年國民黨威權統治、戒嚴台灣 38 年，但他們在戒嚴中不怕被殺被關，為台灣打開民主大門，而今天有強國假借武力說要併吞台灣，他們同樣不怕被殺被關，一定守護這個國家、這片土地，不像有些人，老是長敵人威風，減自己志氣。\n蘇貞昌說，從阿富汗活生生、血淋淋的教訓可以看出來，內部亂，外部也沒辦法幫忙，台灣人要堅定信念，相信只有自己守住這片土地，別人才攻不進來、吞不下去，唯有自助才能人助，別人才有時間協助。\n他表示，總統就任以來，非常重視跟台灣理念相同、價值相同的民主國家互動，而美、日、立陶宛等國都對台灣表達關心；美、日、韓等周邊國家也都表示非常重視台海和平穩定，德不孤必有鄰，台灣人定會堅決守護台灣。\n蘇貞昌說，蔡總統與他一定和台灣人民堅守這片土地，大家別唱衰自己、不要內亂、不要有看台灣會亂或很容易被吃下去的心理，希望大家團結，就像團結對抗疫情一樣。\n蘇貞昌說，全世界變種病毒肆虐的同時，唯有台灣短短 90 天內讓疫情穩定下來，讓確診數只有個位數，這是第2次的防疫成功奇蹟，台灣就是這樣團結一致，也讓想對台灣侵略的外國武力，不要妄想。\n（新聞資料來源 : 中央社）\n",
        keywords=["蔡英文", "國民黨", "總統", "阿富汗", "蘇貞昌", "民主國家", "蔡易餘", "中廣"],
        category="政治",
        media="芋傳媒",
        datetime="2021-08-17",
        link="https://taronews.tw/2021/08/17/771237",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return taronews.TaroNewsNewsCrawler()


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
