# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import worldjournal
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
    name="世界新聞網_1",
    link="https://www.worldjournal.com/wj/story/121347/5679553?from=wj_catelistnews",
    expected_output=NewsStruct(
        title="中鋼7月獲利佳 每天賺3億台幣",
        content="鋼市基本面看好，台灣中鋼營運再噴發，昨日公告7月稅前盈餘90.8億元（台幣，以下同，約3.26億美元），創建廠50年來單月新高，與去年7月虧損2.9億元相比天差地遠；累計前七月稅前盈餘442億元，每股稅前盈餘2.8元。\n\r\n中鋼董事長翁朝棟表示，「鋼市從任何角度看都是榮景」，將旺到明年上半年。中鋼7月獲利佳，顯示中鋼降低成本大作戰奏效，近期再將節省成本的年度總目標調高到45億元，有信心達陣。\n\r\n法人指出，台股進到跌勢整理，鋼鐵股被拖累趨於弱勢，但鋼市基本面強，各重點鋼廠獲利不斷創新高，當前中鋼股價與營運績效重度悖離，還有多家上市鋼廠明顯被低估，市場傳出主力大戶鴨子划水進場布局，外資持股中鋼占比達20.38%、為6月來相對高點，新一波反彈動能箭在弦上。\n\r\n中鋼昨天股價收盤37.65元，跌0.1元。\n\r\n中鋼表示，7月碳鋼銷售量80萬公噸，單月合併營收418億元，月增8%、年增70%，累計前七月合併營收2551億元、年增46%，前7月稅前盈餘442億元，每股稅前盈餘為2.81元，為歷史同期最高。\n\r\n法人分析，中鋼盤價持續走高，雖然7月的內銷持平，但外銷價續漲，而且第3季棒線、鋼板等行情平均調高4.1%，下游提貨超量，7月營運再創新高，自結單月合併稅前盈餘90.84億元，比6月新高再增9%，寫下建廠50年歷史最強紀錄。\n\r\n翁朝棟說，對鋼市前景有充分信心。中鋼營運穩定向上，他認為獲利能不斷走強的主因在於近年超前部署奏效，不管是高值化精緻鋼廠、綠能產業、節能減碳等重點項目都展現成果。\n\r\n另一方面，中鋼全體總動員降低成本，原定全年目標36億元，到7月底已經省下30.34億元、進度超前，因此再將節省成本的年度總目標調高到45億元，有信心達陣。\n\n",
        keywords=["營收", "股價", "綠能"],
        category="財經",
        media="世界新聞網",
        datetime="2021-08-17T02:11:00-04:00",
        link="https://www.worldjournal.com/wj/story/121347/5679553?from=wj_catelistnews",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="世界新聞網_2",
    link="https://www.worldjournal.com/wj/story/121218/5679359?from=wj_catebreaknews",
    expected_output=NewsStruct(
        title="聯亞沒過EUA不意外 專家籲公布資料 避免政治保護力",
        content="聯亞疫苗未通過EUA審核，疫苗2期計畫總主持人、中國附醫副院長黃高彬表示，雖然疫苗不是只有看中和抗體，但當初規則就是這樣訂定；至於聯亞3期臨床試驗的規畫，黃高彬表示，聯亞將在印度進行第3期臨床試驗，而且已經簽約，衛福部目前也同意第3期可在台灣做，應會「雙頭進行」。\n\r\n聯亞疫苗未能通過EUA審查，國產疫苗只剩高端，多位專家不感意外，但為聯亞感到可惜，因著重於中和抗體濃度的EUA審查，可能無法彰顯其細胞免疫反應的優越性。\n\r\n前衛生署長楊志良說，外界質疑高端「政治保護力」優於實際保護力，政府應完整公布高端和聯亞雙方的資料，才能令民眾信服，「沒有完整保護力資料下，大量接種高端就是豪賭。」\n\r\n台灣新冠肺炎疫苗EUA針對確效的兩項標準，一是與接種AZ疫苗者比較，中和抗體平均效價比值，二是血清陽轉率，兩者都必須達標。\n\r\n黃高彬表示，聯亞在兩項標準比較上都有一些差距，「但沒有說差得太離譜」。疫苗不是只有中和抗體，還要考慮T細胞反應，這對長期保護「才是重中之重」；第3期臨床試驗結束，也可能就直接申請藥證，不一定要申請EUA。中研院生醫所兼任研究員何美鄉也說，第三期試驗仍可能證明有效，「趕快做第三期才是王道。」\n\n",
        keywords=["疫苗", "聯亞", "EUA"],
        category="台灣",
        media="世界新聞網",
        datetime="2021-08-17T02:29:18-04:00",
        link="https://www.worldjournal.com/wj/story/121218/5679359?from=wj_catebreaknews",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return worldjournal.WorldJournalNewsCrawler()


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
