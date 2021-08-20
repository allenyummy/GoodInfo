# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import cna
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
    name="中央社_1",
    link="https://www.cna.com.tw/news/afe/202107200398.aspx",
    expected_output=NewsStruct(
        title="台泥完成購併NHΩA 進軍儲能、充電樁市場 | 證券 | 中央社 CNA",
        content="（中央社記者蔡芃敏台北20日電）台泥（1101）完成購併ENGIE EPS，並將更名為NHΩA。台泥指出，透過本次購併進軍儲能、充電樁市場，台泥將成為國內唯一具備綠能、電池、儲能、電動車快充研發與自製能力的全方位能源集團。台泥今天深夜發布新聞稿指出，子公司台灣水泥歐洲控股以每股歐元17.1元，總額合計為1.32億歐元對價，完成對義大利儲能公司ENGIE EPS SA 60.48%股權收購，公司新名稱NHΩA也正式生效。根據彭博新能源財經BNEF（2020）統計，合併NHΩA後，台泥儲能系統建置容量將排名全球第4，也成為國際多功能高端電動車充電樁主要的供應廠商。台泥董事長張安平相當重視這起購併案，不僅率領高階主管前往義大利，更舉行NHΩA交割儀式及主持首次董事會。張安平表示，能源布局不能只看台灣市場，必須具備國際市場競爭力。歡迎新夥伴加入，一起為地球及世界做出改變。台泥指出，透過本次購併，台泥將成為國內唯一具備綠能、電池、儲能、電動車快充的研發與自製能力的全方位能源集團。NHΩA為座落義大利米蘭並於法國上市的儲能公司，擁有全世界最先進BESS（電池儲能系統）技術，與最先進的電動車快充裝置、智慧電網及完整產品線，案場遍布歐洲、美洲、大洋洲及非洲。訂閱《早安世界》電子報 每天3分鐘掌握10件天下事 請輸入正確的電子信箱格式訂閱感謝您的訂閱！台泥指出，NHΩA 與世界第四大汽車公司Stellantis的合資公司Free2Move eSolutions，已積極開展布署南歐最大電動車雙向快充V2G電網，並透過儲能打造最大虛擬電廠。收購NHΩA後，台泥企業團也將成為台灣唯一具有建置長效型、大型儲能系統的公司，提供用電大戶最佳解決方案。台泥的儲能方案預計將為客戶儲存非尖峰或再生能源多餘電力作為備轉容量，將成為用電大戶穩定電力的關鍵要角。（編輯：林治平）1100720",
        keywords=["台泥", "NHΩA", "News", "新聞", "即時新聞", "中央社"],
        category=None,
        media="中央社",
        datetime="2021/07/20 23:59",
        link="https://www.cna.com.tw/news/afe/202107200398.aspx",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="中央社_2",
    link="https://www.cna.com.tw/news/afe/202108110212.aspx",
    expected_output=NewsStruct(
        title="聯發科發表兩款6奈米5G晶片 終端裝置第3季上市 | 產經 | 中央社 CNA",
        content="（中央社記者張建中新竹11日電）手機晶片廠聯發科今天發表兩款採用6奈米製程的5G行動晶片天璣920和天璣810，採用這兩款新5G行動晶片的終端裝置預計第3季在全球上市。聯發科副總經理暨無線通訊事業部總經理徐敬全表示，最新推出的天璣920和天璣810可以提供5G智慧手機強勁性能、智慧顯示和較佳的影像體驗，也為使用者提供先進的5G技術和功能。天璣920採用6奈米製程，擁有強勁性能和低功耗表現，與天璣900相比，遊戲性能提升9%，並支援智慧顯示技術和硬體級的4K HDR影像技術。天璣810也採用6奈米製程，CPU處理器搭載主頻為2.4GHz的Arm Cortex-A76大核，支援先進的拍照特性，與虹軟科技合作的AI-Color技術，可為終端裝置提供AI 景深增強、AI色彩等功能，可創作更精彩的影像作品。徐敬全說，天璣系列5G行動晶片將會持續豐富產品組合。聯發科預計於年底進一步推出採用台積電4奈米製程的5G旗艦級晶片，首款搭載晶片的手機將於2022年第1季量產。（編輯：郭無患）1100811",
        keywords=["奈米", "晶片", "5G", "News", "新聞", "即時新聞", "中央社"],
        category=None,
        media="中央社",
        datetime="2021/08/11 15:57",
        link="https://www.cna.com.tw/news/afe/202108110212.aspx",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return cna.CNANewsCrawler()


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
