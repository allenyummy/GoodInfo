# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import pts
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
    name="公視新聞_1",
    link="https://news.pts.org.tw/article/540373",
    expected_output=NewsStruct(
        title="高端股東會首要強調「增產報國」 其次要國際連結幫助友邦",
        content="\n高端疫苗今天上午召開股東會，總經理陳燦堅強調目前首要目標，就是全力生產增產報國以及國際連結，除了讓國人使用無虞外，也希望能幫助我們的友邦。不過，有專家指出，高端疫苗完整中文說明書，關於保護效期部份，內文卻註明目前保護效期不明，不一定能對所有施打者產生保護作用，認為高端沒有提供相關數據，疫苗保護力讓人質疑。\n高端疫苗上午9點召開股東會，約一小時後順利散會，不少小股東親自參加力挺高端。會後總經理陳燦堅接受媒體訪問，除了感謝股東支持外，他提到高端現階段目標就是衝產量，補足疫苗缺口。高端總經理陳燦堅指出，「第一個就是增產報國，第二個當然就是國際連結，使用無虞的情況下可以幫助我們的友邦。」陳燦堅對高端疫苗品質很有信心，不過上週食藥署公布高端疫苗完整中文說明書，有專家指出，在第四點特殊警語及使用注意事項，關於保護效期部份提出質疑，因為內文中寫著，可提供的保護效期不明，仍須由進行中的臨床試驗進一步確定。另外，在疫苗效果的限制部份，內文也寫著，第2劑高端打完約2周後，開始有中和抗體反應，如同所有疫苗，高端不一定對所有人都能產生保護作用。不過食藥署澄清， 因為高端疫苗主要是緊急使用授權專案製造，尚未完成三期臨床試驗，才會加註相關警語。食藥署藥品組副組長吳明美解釋，「整個第二期臨床試驗的執行期程是要打完第二劑之後6個月，所以數據大概是10月11月期末報告才會出來，那EUA的話就是因為公衛申請緊急情勢，我們要趕快打疫苗產生保護力，不然等到第三期整個都走完的話，可能疫情會影響更大或更嚴重。」食藥署官網上也有提供AZ疫苗、莫德納疫苗中文說明書，翻閱內容，在保護效期、疫苗效果的限制的部份，也有一樣加註相關警語。不過，高段疫苗第6輪疫苗首日接種預約已超過30萬人，部份專家學者認為，是否有保護力，高端仍應完整向國人釋疑。\n",
        keywords=["保護力", "總經理", "臨床試驗", "陳燦堅", "食藥署", "高端", "高端疫苗"],
        category=["首頁", "產經"],
        media="公視新聞",
        datetime="2021-08-17T04:56:15.000000Z",
        link="https://news.pts.org.tw/article/540373",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="公視新聞_2",
    link="https://news.pts.org.tw/article/540195",
    expected_output=NewsStruct(
        title="【更新】五倍券》政院與綠黨團初步達免付1千共識 藍黨團場外喊普發現金",
        content="\n今天上午行政院與民進黨立委召開會議討論五倍券，兩個小時的會議後，民進黨立法院黨團總召柯建銘表示，政院接受各方的意見，確定做出了改變，振興五倍券預計最快十月初發放。根據轉述，蘇貞昌會中定調推五倍券，全民免出一千，柯建銘透露差不多在10月初發放。另外，國民黨立委今天也在行政院外抗議，批評是密室協商，要求普發現金。\n國民黨立委到行政院大門前灑下玩具紙鈔，高喊不要五倍券，普發現金才實在，更要求進入行政院，遭到維安警力阻擋，雙方一度發生推擠、衝突。因為此時，行政院與民進黨立委討論五倍券的會議正在進行中，讓未受邀的國民黨很不滿，批評是密室協商。國民黨主席江啟臣批評，「現在正在密室協商，蘇院長只願意跟執政黨的委員對話，我不曉得他們是派系在對話，還是真的在接受人民聲音、人民的意見。發現金比較實在，發現金最實在，最直接，人民的聲音就是這麼簡單。」行政院副秘書長何佩珊隨後出面與國民黨立委溝通，表示將由副院長沈榮津和他們會面，再度引發藍委們不滿。從上午9點開始進行的會議，進行兩個小時後，總召柯建銘、立委羅致政等人才步出會議室。柯建銘轉述今天會議主要以交流意見為主，總共有45個綠委與會，有30個人輪流發言，政院也接受各方的意見，確定做出了改變。民進黨立院黨團總召柯建銘指出，「今天所有發言，當然對於行政院接受各方面意見以後，做出這樣的改變是確定的，當然有些黨團成員提出一些問題，包括小額、使用多久、使用到什麼時候，包括很細微的面向都有討論。」根據轉述，蘇貞昌會中定調推五倍券全民免出一千，具體的振興5倍券何時發放？柯建銘透露差不多在10月初，並考慮到疫苗覆蓋率，同時也有機會以數位加碼的方式來照顧小商家、小攤商。1900更新行政院長蘇貞昌強調，因為今年經濟成長率預估上修為5.88%，可望創11年新高，因此一千元由政府全額負擔。行政院長蘇貞昌表示，「我們今天(8/16)大家達成共識，就通通不用付1千元，就可以領到5倍券5千元，因為大家已經很習慣5倍券，所以名稱還是叫5倍券，它是限期使用的現金，而且會長高長胖的現金。」至於國民黨提出發現金的訴求，蘇貞昌說，5倍券是有限期使用的現金，透過加碼，協助店家振興又紓困，若像日本那樣發現金被存起來，就比較可惜。\n",
        keywords=["五倍券", "國民黨立委", "密室協商", "普發現金", "柯建銘", "行政院"],
        category=["首頁", "政治"],
        media="公視新聞",
        datetime="2021-08-16T04:56:15.000000Z",
        link="https://news.pts.org.tw/article/540195",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return pts.PTSNewsCrawler()


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
