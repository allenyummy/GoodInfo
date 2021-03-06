# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ustv
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
    name="非凡新聞_1",
    link="https://news.ustv.com.tw/newsdetail/20210816A001044?type=147&",
    expected_output=NewsStruct(
        title="最前線筆記／主力縮手 台股格局如何看？而近期頻殺盤為清洗融資？",
        content="※本文授權自朱思翰粉絲專頁\r\n《8/16大盤表現》\r\n這週台北股市的半年線保衛戰正式開打，不過開盤就出師不利，開低後往下測試，但技術面大家也常說，長天期的均線，多少還是會有一點支撐力道，所以開低之後搶反彈的籌碼湧入，讓指數回到平盤。不過台股近期的殺盤，主要是為了清洗融資，散戶看到回測均線就急著搶進，主力大戶怎麼可能跟風，隨即再殺一波，指數一度大跌超過200點破前波段低，幸好終場跌幅稍微收斂，下跌123點。\r\n\r\n主力資金的縮手，讓台股呈現量縮緩跌的格局，要如何看待？盤中分析師認為，台北股市這一波基本面沒有變，而是籌碼面出現很大問題，再配合到業內主力，針對8/27要上路的當沖示警制新遊戲規則，造成操作手法的改變，如果過了這週，業內主力仍不願拉抬指數，那麼月季線死亡交叉恐怕就會造成整理期，拉長到三個月左右！\r\n\r\n不過今天比較特別的，除了要關注盤後融資籌碼變化外，也能發現近期，散戶反而比較不愛操作的個股，沒有需要洗融資的，股價反而不受影響，不只台積電沒有賣壓，台塑、南亞也沒賣壓，先前外資為了「壓指數」而摜殺的權值股，今天大多表現抗跌，還有下半年業績看俏的個股，也率先做出反彈，往好處想，就是至少能對利多有反應。\r\n\r\n像是重建題材的中鋼構(2013)，疫苗開打題材的高端(6547)，MCU缺貨題材的新唐(4919)、九齊(6494)，MOSFET富鼎(8261)、杰力(5299)，車用整流二極體的強茂(2481)等等，再殺可能都已經低於其價值了，所以明顯有買盤支撐，不僅能在逆風中抗跌，之後也有機會先反彈。雖說台股可能因為主力不攻，而拉成整理時間，但手上有業績題材個股的朋友，像是擁產能的車電股，蜀芳老師認為，除非你是融資，不然真的不用殺低，依自己的資金狀況來做調整。\r\n\r\n不過若是講到記憶體，今天華邦電、旺宏等，都終結了日Ｋ連黑，終於收紅Ｋ棒，在多空交雜之下，報價看來仍不穩定，今天的收紅還是要先以反彈視之比較安全。另外近期股價修正的聯電，老師認為還是以7/30的大量低點55.8元作為防守關卡，持續觀察。\r\n\r\n最後談談貨櫃航運，老師們大多認為這個月是反彈黃金期，畢竟貨櫃三雄的當沖占比仍高，在8/27的當沖示警機制上路之前，如果沒有比較明顯往上表態，那麼對於貨櫃三雄後續的走強相對不利。不過畢竟貨櫃三雄現在都是橫盤整理，所以股價拉高時，不要忘記得站在賣方，如果在低檔就別再殺低。\r\n\r\n也提醒大家，最近貨櫃三雄的均線糾結，參考價值會越來越低，當均線跌破時不仿就用價值面來計算股價，基本上高檔150元左右一定會有反壓，或是參考文恩老師在盤中提供給大家，航運指數的日關鍵價做為參考，今天運輸指數盤中破了255點支撐，也沒收上259.85的日關鍵價，更不用說尾盤的下殺，導致長榮與陽明都收在今天的均價之下，明天就算開高，也切記不能追！恐怕都是到今天的均價附近，就會有賣盤的壓力，亂買小心套在最高點！\r\n\r\n（看更多最前線每日筆記：https://www.facebook.com/anchorszuhan/）",
        keywords=None,
        category=None,
        media="非凡新聞",
        datetime=None,
        link="https://news.ustv.com.tw/newsdetail/20210816A001044?type=147&",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="非凡新聞_2",
    link="https://news.ustv.com.tw/newsdetail/20210816A098?type=144&listOnly=true",
    expected_output=NewsStruct(
        title="台股修正布局 鎖定高價股ETF迎反彈契機",
        content="台股近日走勢震盪，從過往經驗來看，當股市面臨修正，高價股股本相對小，加上多數企業為績優龍頭股，所以修正後反彈速度也較快，國內投信業推出，鎖定高價股的ETF，挑選具備公司財務體質佳、股利發放穩定，同時還是熱門零股標的，讓預算有限的投資人，也能掌握高價股的成長動能，同時做到風險分散。全球變種病毒肆虐，加上市場關注聯準會最新動向，衝擊投資人信心，台股也不可倖免陷入高檔盤整，不過觀察過去當股市面臨修正時，高價股股本相對較小，修正後反彈速度也較快，隨著進入電子產業旺季，專家建議鎖定高價股ETF，掌握反彈契機。\r\n\r\n中信小資高價30經理人張逸敏：「半年線這邊應該會有支撐力道，所以短期台股的部分，可能會先以盤代跌的狀況，然後再度在第三季身邊的大家觀察，企業獲利表現之後再看上攻的機會，短期內大家可以再度在觀察籌碼面，另外一方面，投資人比較沒有空觀察個股的話，我建議是可以投資ETF。」\r\n\r\n儘管台股適逢修正，但電子股半導體缺貨漲價效應持續，千金股如不斷電系統大廠旭隼、股王大立光、電商龍頭富邦媒，還有信驊、力旺等標的，依舊是市場熱門話題。\r\n\r\n看看ETF追蹤的，臺灣指數公司特選小資高價30指數，近3年表現，不只高於台灣電子報酬指數，也跑贏台灣加權報酬指數，因為指數除了篩選，公司治理評鑑優良企業，同時也很注重財務體質等基本面。\r\n\r\n中信小資高價30經理人張逸敏：「稅後純益大於零，而且ROE跟股利成長會在我們前80%，才會留在我們的成分當中，最後一項篩選機制就是，挑選零股熱門交易中，前50%的成分股，我們成分股的部分的話，大概有接近六成，是落在半導體族群，電子相關成分股的話大約是落在80%，剩下接近20%，是在傳產股的部分」\r\n\r\n從ETF成分股近四季平均營收來看，長期表現強勢，顯著高於大盤平均值，主要就是因為指數成分股，像是信驊、富邦媒，以及聯發科、儒鴻等高價股多為產業龍頭股，成長動能佳、法人持有率也高，專家建議適當配置，才能掌握台股多頭趨勢，不過也提醒，投資要留意相關風險。（記者黃友柔、謝隆証／台北採訪報導）",
        keywords=None,
        category=None,
        media="非凡新聞",
        datetime=None,
        link="https://news.ustv.com.tw/newsdetail/20210816A098?type=144&listOnly=true",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ustv.USTVNewsCrawler()


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
