# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import bnext
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
    name="Meet創業小聚_1",
    link="https://meet.bnext.com.tw/articles/view/44652",
    expected_output=NewsStruct(
        title="成立保健食品電商、面對下滑股價，尚凡在PTT鄉民法說會如此解釋",
        content="以知名交友網站愛情公寓起家的尚凡國際於昨（19）日舉辦「史上首場PTT鄉民法說會」，短短10日報名人數突破1,000位，也沒有發生尚凡董事長張家銘害怕的「千人響應，一人到場」情況。現場更準備了500份雞排、珍奶，以及聽了有點尷尬的「鄉民梗」讓所有參與者共襄盛舉。\n張家銘表示，從尚帆上櫃以來飽受許多質疑，最主要的原因仍是股價從164元掛牌，一路跌至19.4元，許多股版（Stock）鄉民要他「出來面對」。而在尚凡股價一路上衝，截至截稿前為244元，張家銘也決定出來面對鄉民，解釋尚凡上櫃以來的轉型之路。\n2013年，主力為愛情公寓的尚凡宣布上櫃，首日收盤還有187元的成績，但之後每況愈下。「大家都說我們虧了33個月，5278（尚凡股票代號）是個騙局。」張家銘說。\n他也大方承認上櫃後尚凡所遭遇的劇烈變局，就是「PC轉向行動」的趨勢，「當時又被Garena旗下的BeeTalk（交友App）打到，我們只有兩個選擇，不投資手機App；或是虧損2-3年，但是加大投資App。」張家銘選擇了後者。\n因此他們花了三年時間，第一年招兵買馬，研發產品；第二年，大幅度拓展國際市場；第三年，收斂國際市場。\n產品方面，以App與後續加入的直播服務為最重要的轉捩點，靠著大量的打賞（donate）分潤，拉動尚凡的營收。\n在國際市場方面，尚凡最多同時經營20個海外市場，包含日本、墨西哥、阿根廷、韓國等，於其中找尋投資報酬率較高的市場。值得注意的是，尚凡幕後的投資者包含日本CyberAgent，由旗下的mixi株式會社進行日本推廣，但至今仍不算成功，「日本真的很難打。」張家銘說。\n而在收斂國際市場，專注於投資報酬率較高的地區，尚凡也大幅縮小虧損，2018年的合併營收為8.92億元，同比2017年的4.8億成長近乎一倍。在股利方面，更追隨台積電每季分配的模式，「股利發好、發滿。」張家銘笑著用鄉民梗說。\n張家銘也在現場同步展示了尚凡旗下的所有產品，包含iPair App，於兩年前加入直播功能後，已經是營收主力。也有許多主播出席本場法說會，展示了在短短幾分鐘內就獲得數萬元打賞的吸金能力。\n其他如以結婚為前提的SweetRing交友、瞄準新鮮人與大學生的WeTouch交友，以及目前免費，尚未貢獻營收的網紅人力銀行Kool。張家銘提到，由於前幾年招募了許多優秀的工程師，並鼓勵內部創業，尚凡現在每年都有能力做出1-2款產品。\n最特別的是尚凡旗下瞄準保健食品的大研生醫，主打健康、美容、運動、纖體四大系列。根據張家銘的說法，大研生醫並沒有要賺大錢，也不會大幅虧損，初衷是希望親朋好友能夠身體健康。此外，更為了「透明化」公布利潤，大研生醫的保健食品成本是售價30-40％、經銷商回饋金約50-60％，剩下約為10％利潤。「我們也有葉黃素。」他補充說道。\n同時張家銘也在現場接受提問，以下為整理過後的部分問題：\nＱ：與其他直播平台的差異化？\n我們base在交友需求上，主播跟粉絲就是一家人、好朋友。我們許多粉絲跟粉絲間、主播跟主播間都認識，是跟其他比較不一樣的地方。17、浪Live比較偏向才藝、明星，我們則是大家都像是好朋友。\nＱ：如何面對直播泡沫化？\n目前沒有觀察到直播走向泡沫化的現象，除非有一天男生對女生都沒有興趣，那我們的男主播也許會變多。\nＱ：大研生醫的供應商？\n要透明絕對沒有問題，供應商都是生展在內的上市櫃公司。\nＱ：衝高2019年獲利的具體方法？\n持續投資報酬率比較高的市場。",
        keywords=None,
        category=["社群服務", "新零售"],
        media="Meet創業小聚",
        datetime="2019-03-21T09:05:00+0800",
        link="https://meet.bnext.com.tw/articles/view/44652",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="Meet創業小聚_2",
    link="https://meet.bnext.com.tw/articles/view/47657",
    expected_output=NewsStruct(
        title="護國神山的破壞式創新：當摩爾定律到極限後，台積電是如何超越Samsung、Intel的？",
        content="一直以來，台灣的人才在國際上享有盛名，從硬體開發到軟體工程師都是世界頂尖級別，台灣跟著世界前行，也貢獻了改變世界的力量。《打造創新路徑》一書紀錄了1970年代以降，台灣科技產業的創新故事，宏碁、神通、大眾、台積電等大企業是如何看見世界趨勢的？他們的經驗可以現在的我們什麼借鏡？\n超越摩爾，2011～2019年：28 奈米之後，台積電進入了另一個發展時期。在這之前，台積電以及他的主要晶圓代工對手，如聯電、Global Foundries、中芯國際等，都在由摩爾定律所制訂的藍圖上，努力追趕以拉近與國際大廠的距離。\n當然，即便許多人開始認為摩爾定律已經慢慢的逼近其物理極限（Huang, 2015），依附它而發展起來的台積電也不可能一夕之間就能自由自在的另謀他就，只是要設法讓它繼續走下去的難度越來越高。過去台積電還可以跟在 Intel 背後，但是自從 28 奈米以後，Intel 似乎也越來越跟不上摩爾定律的腳步，尤其到了 10 奈米之後，台積電只能在和 Samsung 的競爭過程中探索未來的方向。競合關係的轉變，也讓台積電的策略慢慢的從被動跟隨轉變而為主動出擊。例如台積電在 20 奈米採用雙重曝刻（double patterning），或是 3D 結構的鰭式場效應電晶體（FinFET）。另外如台積電所推出 3D 的封裝技術，可以整合多顆晶片的整合型扇形封裝（integrated fan out；InFO），並搭配自行開發的 CoWoS（chip-on-wafer-on-substrate）製程技術，都是延續台積電的過往能力軌跡再推展摩爾定律的重要事件。\n相對地，已經走在技術前端的台積電，卻能立刻就建立起 RISC 處理器的產線。剛開始台積電取得 Qualcomm 手機晶片的訂單，而早期 iPhone 的晶片則是都由 Samsung 代工，但是自從 2014 年的 A8 晶片開始，台積電藉由先前 28 奈米順利切入智慧型手機市場，因此得以打入 Apple 的供應鏈。自此之後，台積電在高階的 ARM 架構手機晶片中擁有超過一半的市佔率，2019 年時，華為首款的 5G 晶片麒麟 990、Qualcomm 的 Snapdragon（驍龍）855 晶片、Apple 的 A13 晶片等，都是由台積電生產，幾乎是 ARM 架構的陣營中最大的製造商。",
        keywords=None,
        category=["硬體", "商業模式"],
        media="Meet創業小聚",
        datetime="2021-05-04T15:41:00+0800",
        link="https://meet.bnext.com.tw/articles/view/47657",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return bnext.BnextNewsCrawler()


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
