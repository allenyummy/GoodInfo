# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import cynes
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
    name="鉅亨新聞網_1",
    link="https://news.cnyes.com/news/id/4520040",
    expected_output=NewsStruct(
        title="沖壓件廠今年發CB籌資 合計募集金額達21億元",
        content="今年下半年沖壓件廠接連發行可轉換公司債 (CB) 籌資，聯德 - KY (4912-TW) 完成發行 7 億元無擔保可轉換公司債 (CB) 後，包括和勤精機 (1586-TW) 擬發債籌資 4 億元、佳穎精密 (3310-TW) 擬發債籌資 6 億元，都已申報生效募集中，安力 - KY(5223-TW) 新建廠案最新籌資計畫，也由董事會確定發行 CB 籌資 4 億元，合計四大沖壓建廠今年籌資達 21 億元。\n聯德 - KY 生產金屬沖壓製程產品，主要應用在資料中心、伺服器、手機及雙輪電動車輛散熱相關，由於 5G 通訊手機需要更高散熱效率，推升沖壓散熱組件產品出貨成長的動能。聯德 - KY 發行的 CB 籌資案順利完成募集，為今年首檔掛牌交易的金屬沖壓件度籌資案，其他沖壓件廠如和勤精機辦理發債進行市場籌資案，也正在進行中。\n佳穎精密是台股少數跨足營建業務的精密沖壓件廠，已向金管會送件擬發行有擔保可轉換公司債籌資 6 億元，主辦券商富邦證券，此市場籌資案件申報生效後，依時程估算最快 9 月底完成。\n安力 - KY 今年上半年財報每股純益 2.66 元，僅次於聯德 - KY 的每股純益 2.89 元，第 2 季稅後後純益為 1.07 億元，創新高，季增 11.52 倍，年增 2.72 倍，每股純益 2.47 元；安力 - KY 今年上半年出貨美系筆電客戶舊機種，7 月新舊機種一併出貨，營收衝上 2.03 億元，月增 13.93%，年增 52.14%，前 7 月營收 10.15 億元，年增 30.8%；預估 8 月營收也在歷史高檔水準。\n安力 - KY 目前訂單以筆電應用為主，客戶涵蓋台達電 (2308-TW)、蘋果等，訂單能見度達第 3 季，估營收可逐季成長，安力 - KY 也積極進行市場多元布局，鎖定中國內需市場，切入包含民生、5G 光纖、伺服器、電動車等領域，繼重慶廠擴廠後，浙江新廠已投入興建中，預計 2022 年完工。\n安力 - KY 2019 年底完成重慶二期廠房建設，增加粉體塗裝生產缐，董事長許振焜表示，產線完成後將可迎接中國內需汽車零組件市場需求。\n",
        keywords=["CB", "籌資", "沖壓件廠", "聯德", "安力"],
        category=None,
        media="鉅亨新聞網",
        datetime="2020-09-01T12:48:46+08:00",
        link="https://news.cnyes.com/news/id/4520040",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="鉅亨新聞網_2",
    link="https://news.cnyes.com/news/id/4537458",
    expected_output=NewsStruct(
        title="沖壓件廠今年以來市場籌資達21億元 擴廠迎新商機",
        content="沖壓件廠安力 - KY(5223-TW) 上月底完成發行 4 億元無擔保可轉換公司債市場籌資案，為今年來第四家完成籌資的業者，合計今年以來沖壓件業者自市場籌資 21 億元，在銀彈支援下，將陸續擴廠迎接新商機。\n今年以來，包括聯德 - KY(4912-TW)、和勤精機 (1586-TW) 及佳穎精密 (3310-TW) 、安力 - KY 的發行可轉換公司債籌資均已完成，其中聯德 - KY 發行 7 億元可轉債規模最大，佳穎精密 6 億元居次。\n安力 - KY 積極進行市場布局，鎖定中國內需市場，切入包含民生、5G 光纖、伺服器、電動車等領域，繼重慶廠之後，並投入在浙江省湖州市興建廠房，籌資目的即為支應新廠建廠所需。廠房興建完成後預計將昆山廣禾的生產設備移至湖州安力新廠，用於金屬壓鑄件生產，並設置電著塗裝之金屬表面處理產線，而昆山新力廠及湖州安力廠均有多餘空間滿足未來銷貨客戶的訂單需求，且也能完善規劃智能工廠，安力 - KY 湖州新廠預計在 2022 年完工。\n安力 - KY 的成長動能除 NB 外，今年也順利增加家用遊戲機新應用，散熱零件布局已見成效，預估今年營收貢獻度將達 8%，明年估營收成長帶動下，家用遊戲機散熱零件營收占總營收比重將逾 10%。\n和勤精機產能遍布兩岸，中國嘉興和新、淮安和新兩廠專注生產汽車、電動車零件，台灣新建的彰化全興廠則是集團總部，生產硬碟及自行車精密零件等高階產品，2019-2020 年兩岸資本支出金額達 14.4 億元，預期 4 年後的集團營收倍增。其中，和勤中國嘉興和新廠第 5 車間擴產計畫，預計總投資金額約新台幣 5 億元，明年完工提升產能後，嘉興和新廠年產值將可拉高到 40 億元。\n和勤精機台灣彰化全興廠則規劃投資金額 9.44 億元，包括購置彰化全興工業區既有的既有廠房作為擴產基地，其餘資金將陸續投入廠房增建、投資設新備，和勤精機為全興廠的擴充產能年完全開出，也正開發醫療與電子產品應用認證。\n聯德 - KY 在手機散熱產品製程上，將銅管製程推向散熱板及加工難度高的不銹鋼管，今年因應客戶需要，將全力生產出貨；去年營收 49.93 億元，年減 17.37%，今年除開始出貨給國際航太業者，台灣電動機車電池模組與車架也開始出貨，新客戶新產品今年將陸續發酵，營收貢獻也逐步展開。\n法人估，聯德 - KY 在菲律賓等海外布局逐步完成，同時新產能到位，在手機、散熱與伺服器滑軌等新客戶、新訂單增加下，今年營收將較去年成長。\n",
        keywords=["沖壓件", "CB", "籌資"],
        category=None,
        media="鉅亨新聞網",
        datetime="2020-11-01T12:57:01+08:00",
        link="https://news.cnyes.com/news/id/4537458",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return cynes.CYNESNewsCrawler()


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
