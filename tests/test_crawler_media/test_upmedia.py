# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import upmedia
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
    name="上報_1",
    link="https://www.upmedia.mg/news_info.php?SerialNo=121668",
    expected_output=NewsStruct(
        title="【時間軸】美軍撤軍阿富汗後　神學士只花一個月武力奪權--上報",
        content="\n\n\n\n\n\n\n \n編按：美軍在7月2日倉皇地撤出阿富汗最大基地巴格拉姆空軍基地，儘管拜登政府稱會持續支持阿富汗政府，但沒想到短短一個月左右，在8月15日武裝團體神學士就進入首都喀布爾，喀布爾不戰而降，美軍扶持的阿富汗政府在短短一個月左右垮台，《上報》整理關鍵事件時間軸，回顧這一個月的關鍵事件。\n \n\n \n關鍵報導\n \n阿富汗神學士造訪中國 王毅期許能與新疆獨立運動劃清界線\n \n王毅在會談中先是批評了美國與北約倉促撤軍「實際上標誌著美對阿政策的失敗，阿富汗人民有了穩定和發展自己國家的重要機遇。」\n \n\n神學士代表團在天津會見王毅。（中國外交部）\n \n阿富汗神學士奪下鄰巴基斯坦邊境第二大關卡 美國準備撤出2500名當地翻譯員\n \n一名神學士士兵表示「經過20年美國的殘暴以及他們的走狗之後，斯平布爾達克再度被神學士拿下...聖戰士（Mujahideen ）和人們的頑強抵抗迫使敵人逃跑，看阿，那是伊斯蘭酋長國的旗幟。」\n \n神學士奪下阿富汗鄰巴基斯坦第二大關卡。（湯森路透）\n \n \n【神學士擴張版圖】美將領公開警告 撤軍將導致阿富汗內戰惡夢再起\n \n始終不信任神學士的指揮官表示，倘若真的將部隊全數撤離，必然讓阿富汗政府失去依靠與協助，如今的神學士，一方面藉由和談、拖延爭取時間，另一方面又不斷在國內「開疆闢土」，打從5月份至今，該團體已經掌握阿富汗370個行政區當中的50個，勢力愈來愈逼近首都喀布爾（Kabul）。\n \n駐紮阿富汗的美軍，將在9月11日全數撤離。（湯森路透）\n \n \n \n \n \n \n \n \n \n \n \n \n",
        keywords=["阿富汗", "神學士", "塔利班", "甘尼", "美國", "美軍"],
        category="國際",
        media="上報",
        datetime="2021-08-16T12:50:00",
        link="https://www.upmedia.mg/news_info.php?SerialNo=121668",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="上報_2",
    link="https://www.upmedia.mg/news_info.php?SerialNo=121781",
    expected_output=NewsStruct(
        title="設立海外秘密監獄？　中國女子稱在杜拜被中國使館帶到小黑屋關押8天　--上報",
        content="\n\n\n\n\n\n\n \n《美聯社》報導訪問一名中國女性，指稱中國政府在杜拜設立秘密監獄，裡面關押維吾爾人。\n\n \n該名稱為吳姓女子（Wu Huan）今年26歲，因為未婚夫是中國異見人士，因此嘗試逃離被遣返回中國。該名女子向美聯社透露自己是在杜拜的飯店遭到綁架，並且被中國官員監禁在一棟由別墅改裝的監獄內，他同時在關押地點發現有另外兩名維吾爾人囚犯。\n \n吳姓女子稱，在關押期間，她遭到訊問以及被迫簽屬法律文件虛假指控未婚夫騷擾她。在6月8日她終於被釋放出來，現在人在荷蘭尋求庇護。\n \n她的未婚夫今年19歲，因為在網路上張貼貼文質疑中國官媒對2019年香港抗議的報導以及中印邊界衝突而遭到中國官方追捕。兩人實際上並非維吾爾族人而是漢人。\n \n\nA young woman says she was held at a Chinese-run secret detention facility in Dubai along with at least two Uyghurs. The account is the only testimony known to experts that Beijing has set up a so-called \"black site\" in another country. https://t.co/sPqcXlmHqO\r\n— The Associated Press (@AP) August 16, 2021\n\n \n事發經過\n \n根據吳姓女子說詞，她是在5月27日在自己入住的飯店遭到中國官員訊問，接著被杜拜警方帶到警局後關押三天，期間個人手機和財物暫時遭到沒收。\n \n到了第三天，一名自稱來自中國駐杜拜領事館的人員來拜訪她，並詢問她是否接受外國資金來反對中國。她則回應她非常愛國。接著吳姓女子被使館人員扣上手銬押上一台TOYOTA，接著開了半小時載到郊區一間白色的別墅，從外面看到房間窗戶被改成單獨監禁房間。\n \n接著她被帶到小房間，門被改成重金屬門，屋內只有一張小床，而只有在送食物時才會被打開。另外她被帶去另外一個房間接受訊問好幾次，所有的人都戴口罩因此看不清楚面貌。\n \n在監禁期間，她聽到有維吾爾族人婦女用中文大喊「我不想回到中國，我想回土耳其。」\n \n最後她被迫簽下一份阿拉伯文與英文的文件，聲稱她的未婚夫騷擾她。\n \n\n#Uyghurs in Turkey have been doing a campaign, called ' Where Is My Family?' over the past months, to seek the whereabouts of their family members in East Turkistan. They go to every corner of Turkey, to spread and raise the awareness of Uyghur Genocide. @MeryemFaruh8111 @hrw pic.twitter.com/zrNzQvDXBN\r\n— UyghurInfo (@UyghurInfo) August 14, 2021\n\n \n中國小黑屋延伸海外？\n \n這是首次有人提出證詞中國在海外設立「小黑屋」，類似場所在海外國家，這種場所通常是官方請人去「喝茶」，意味著官方透過非正式手段進行訊問逼供，被請去的人不會有律師資源也不會有收到法院傳票。中國官方經常藉此恐嚇上訪人士。\n \n報導指出，美聯社尚無法核實吳姓女子的說法，吳姓女子也無法指出該場所的具體位置。但美聯社掌握證據指出中國官員訊問她的對話紀錄，以及她從監獄傳送訊息求救的簡訊。\n \n中國外交部發言人華春瑩在16日記者會上否認這件事情，但該提問並沒有在外交部官方紀錄上公開。\n \n抗議者在紐約聲援遭到關押的維吾爾人。（湯森路透）\n \n另外，杜拜當地警方也否認協助中國逮捕該名女子，並稱該名女子在三個月前已經自由地離開了杜唄。「杜拜不會在沒有國際接受的程序和當地執法程序之下逮捕任何外國公民，也不會容許外國政府設立任何拘禁場所。」\n \n報導訪問了中研院法律研所的陳玉潔助教，她表示儘管她未曾聽說過中國政府把類似場所設立到另外一個國家，但這符合中國政府常用各種官方或非官方手段把特定人士抓回國的企圖。\n \n近年來，國際上傳出不少中國政府試圖把維吾爾族人抓回國的案例，包括土耳其、沙烏地阿拉伯等維吾爾族人逃難的目的地國。根據維吾爾人權組織統計，1997到2007年之間公開資料有89名維吾爾人從9個國家遭到遣返回中國，從2014年至今則攀升到了20個國家1327人。\n \n中國在新疆設立可容納數十萬人的「再教育營」，國際社會指責該設施類似集中營，犯下非法監禁、文化滅絕等嚴重侵犯人權的罪刑。\n \n\nThanks to @ChinaFile for the invitation to write about this important subject. https://t.co/r5XnQQtJdW\r\n— Yu-Jie Chen (@yujiechentw) July 30, 2021\n\n \n報導指出，杜拜也有遣返維吾爾族的紀錄，一名法律倡議者Radha Stirling稱她曾協助多名來自印度、約旦等地的公民曾被杜拜秘密拘禁。\n",
        keywords=["杜拜", "維吾爾", "中國"],
        category="國際",
        media="上報",
        datetime="2021-08-17T13:00:00",
        link="https://www.upmedia.mg/news_info.php?SerialNo=121781",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return upmedia.UpMediaNewsCrawler()


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
