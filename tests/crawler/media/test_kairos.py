# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import kairos
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
    name="風向新聞_1",
    link="https://kairos.news/350866",
    expected_output=NewsStruct(
        title="中研院院士閃辭疫苗審查委員引各界關注",
        content="\n\n更多分享工具...國產疫苗何時上市，近期引起國人熱烈討論，中研院院士陳培哲原為國產疫苗審察委員，但近日卻閃退國產疫苗審查委員，他說，委員會已不能維持獨立性與專業性，因為最大困難來自蔡英文總統的壓力。\n家庭主流化聯盟召集人曾獻瑩表示，陳培哲是中研院院士、台大醫學系學士、美國賓夕凡尼亞大學博士，也是現任台大臨床醫學研究所教授、台大醫院內科主治醫師，是真正的專家。\n曾獻瑩說，根據陳培哲的意見，國產疫苗廠商：高端、聯亞和國光，都是研發蛋白質次單位疫苗，但是目前世界衛生組織（WHO）並未認可蛋白質次單位疫苗。連擁有世界上最好蛋白質次技術的美國知名生技公司諾瓦瓦克斯（Novavax），在完成部分第三期臨床試驗後，都未能得到美國食品藥物監督管理局（FDA）認證，也就是無法獲得國際認可。\n陳培哲也斷言，除非諾瓦瓦克斯能獲得FDA核准，否則台灣的國產疫苗也不會成功，關鍵問題在於蛋白質平台是所有疫苗中治療效果與保護力最差的，也不容易生產，但偏偏台灣選了最難的去做。\n曾獻瑩認為，若不是陳培哲這麼清楚的說出來，大眾大概也不會知道國產疫苗的現況，但忠言逆耳，最後陳培哲選擇從防疫第一線的疫苗審查團隊中退下，再看另一位防疫專業人士葉彥伯。\n曾獻瑩表示，葉彥伯是國內少數兼具醫師身份和公衛博士的衛生局長，歷經彰化縣四任藍綠縣長，在他任內，他成功處理了三聚氰胺毒奶粉和塑化劑事件。\n曾獻瑩說，葉彥伯為了未來的防疫做真正的「超前部屬」，早已與台大公衛學院合辦長達16年的萬人血清抗體檢測。新冠肺炎疫情剛爆發，在當時的血清抗體檢測報告中，他提前透露有陽性個案，但是指揮中心卻以地方違背中央「有症狀才採檢」的篩檢政策，最後，政風單位調查葉彥伯，舉國譁然。\n曾獻瑩說，葉彥伯被側翼追殺，被網軍霸凌，最終在鏡頭前近乎「討饒」，請求高抬貴手，兩度哽咽說自己「只是想為防疫多做一點事」。\n曾獻瑩認為，兩位都是防疫的專業人士，可以說是我國難得的人才，卻在這場防疫大戰中，紛紛敗下陣來，然而可能有更多的專業人士被迫選擇閉口不言，是他們的專業不夠嗎？還是因為政治不正確呢？\n曾獻瑩認為這造成了今日台灣新冠死亡率高於全球，也造成了疫苗採購不足窘況，全民現在人心惶惶，經濟受創的基層民眾苦不堪言。我們需要的是防疫的專業來打贏這場仗，但又是誰謀殺了台灣的防疫專業？\n（記者郭大衛／綜合報導）\n更多分享工具...Facebook 留言 則留言\n",
        keywords=None,
        category=["台灣", "政治"],
        media="風向新聞",
        datetime="2021-06-09T10:08:26+00:00",
        link="https://kairos.news/350866",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="風向新聞_2",
    link="https://kairos.news/368246",
    expected_output=NewsStruct(
        title="疫情肆虐！民眾繃緊神經　預期性焦慮大爆發",
        content="\n\n更多分享工具...新冠疫情肆虐全台，許多民眾繃緊神經，不敢就醫看診。一名40歲的王先生固定服用降血壓藥物，現今卻因院內感染爆發，懼怕回診，家人擔心王先生健康，於是陪同就醫，但就快到達醫院大樓時，王先生竟然心跳開始加速，腳也不斷發抖，甚至出現胸悶吸不到氣，嚇壞所有人。求助精神科，經評估有「預期性焦慮症狀」，經過三個月藥物及心理治療後，症狀獲得大幅改善\n身心診所院長楊聰財醫師表示，預期性焦慮症狀屬於廣泛性焦慮症的一種，患者常常會對未來可能發生的事或不幸的事件而出現持續的害怕感，甚至出現胡思亂想，雖然自己想控制這些念頭，但通常不易成功，於是出現坐立不安、呼吸急促、肌肉緊繃、心悸、甚至發抖等預期性焦慮症狀，建議就診尋求解決之道。\n新冠疫情持續一年多，只要出現群聚感染事件，就會有不少民眾因擔心害怕感染而出現預期性焦慮症狀，就醫人數會比平常多二成。今年4月發生的鐵路重大交通意外，也有不少民眾對搭乘大眾交通工具出現預期性焦慮症狀而前來就醫，嚴重影響日常生活品質，提醒民眾千萬別輕忽。\n楊聰財解釋，最常見的預期性焦慮症狀就是出現在失眠患者身上。針對預期性焦慮症狀建議採用「三身三式」技巧來改善，所謂「三身」分別為起身、淨身、養身，再個別對應三種行動。\n「起身」就是迅速離開焦慮環境，透過洗手、沖臉，將焦慮的情緒轉移到身體，達到緩和情緒效果；「淨身」則是透過腹式呼吸、寫心情日記，或是打掃雜亂環境，讓心理獲得平靜效果；而「養身」則是掌握能吃、能睡、能動原則，讓身心維持平衡和健康。\n楊聰財提醒，若預期性焦慮症狀若持續惡化，甚至影響日常生活，就建議要接受藥物及認知行為治療，同時也建議患者家屬應陪同患者參與治療，善用周遭親朋好友的力量，才能有效改善症狀恢復生活品質。\n（記者畢翠絲／台北報導）\n \n \n更多分享工具...Facebook 留言 則留言\n Tags失眠 焦慮 預期性焦慮症\n",
        keywords=["失眠", "焦慮", "預期性焦慮症"],
        category=["健康", "台灣", "生活"],
        media="風向新聞",
        datetime="2021-07-28T08:46:36+00:00",
        link="https://kairos.news/368246",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return kairos.KairosNewsCrawler()


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
