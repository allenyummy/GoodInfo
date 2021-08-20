# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import cnews
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
    name="匯流新聞網_1",
    link="https://cnews.com.tw/209210813a01/",
    expected_output=NewsStruct(
        title="【有影】股市/鴻海H1獲利創史上同期新高！分析師：1982年起已贏在起跑點",
        content="\n\n分析師/吳官隆\n鴻漸於陸無比富，海量千萬人相助，\n無我執著有富足，敵都欽佩金鐵鑄。\n大家好，我是吳官隆，今天聊到鴻海，現在是第一集。\n最近鴻海非主管年薪公開！2021年6月證交所公開資訊觀測站，公布2020年上市公司非主管職員工薪資，鴻海與旗下的鴻準都排進年薪前十名，鴻海非主管職員工平均年薪為241萬元，讓一堆人驚訝的優渥。\n﻿\n為鴻海建立起中央法務處，400人法務大軍的前法務長周延鵬，8月因病過世享年61歲。在郭董指導周延鵬建立的法務大軍助攻，鴻海營收：1991年股票上市時的新台幣23億元，到2002年飆升107倍至新台幣2578億，最近2020年衝上至新台幣5兆3600億元。\n1974年，郭董母親初永真女士，以標會得來新台幣10萬元資助郭台銘創業，成立鴻海塑膠企業有限公司。當時的員工10人，主要業務為製造黑白電視機旋鈕。1981年，鴻海塑膠轉型生產個人電腦連接器。1982年，鴻海塑膠改名鴻海精密工業股份有限公司，註冊資本額達到1600萬元。1985年，鴻海設立美國分公司。\n從統計數字看：1978年到2014年，居民消費價格指數CPI為105。物價每年上漲5%，37年間物價變為原來的6倍。2014年的1萬元，相當於1978年的1600元，反之1978的1萬元，相當於2014的6萬元。\n所以1978年的1600萬元，大約等於2014年的1億元，根本是天文數字，證明鴻海1982年，已經是讓人望塵莫及的存在。\n➤【鄉民投資客】Youtube播放清單\n《更多CNEWS匯流新聞網報導》\n【有影】股市/風電「國家隊」整備出發？四大指標廠商喜迎Q4旺季？｜鄉民投資客\n【有影】股市／取消7月夏季電價…太陽能股旺季何時來？分析師揭進場「關鍵時間」｜鄉民投資客\n【文章轉載請註明出處】\n\n",
        keywords=["股市分析", "鴻海", "鴻準"],
        category=None,
        media="匯流新聞網",
        datetime="\n\n2021-08-13\n",
        link="https://cnews.com.tw/209210813a01/",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="匯流新聞網_2",
    link="https://cnews.com.tw/003210720a10/",
    expected_output=NewsStruct(
        title="郭董、台積電的BNT青少年打不到？  食藥署長證實「差一步」快來辦",
        content="\n\n匯流新聞網記者陳鈞凱／台北報導\n郭董、台積電出面洽買到德國BNT疫苗各500萬劑要捐贈給政府使用，由於BNT疫苗是目前檯面上唯一可供12到18歲施打的疫苗，陳時中已宣示將保留給青少年族群，但現在傳出食藥署還沒接到變更適應症的申請，究竟台灣囝仔打不打得到？食藥署長吳秀梅今（20）日傍晚強調，只要上海復星提審書面資料「疫苗快到之前再做申請一樣來得及」。\n台灣目前到貨的AZ疫苗與莫德納疫苗，適應症都是18歲以上成人，不包括青少年或學生在內，因此，BNT疫苗未來到貨預計留多少給青少年施打？一向備受關注，中央流行疫情指揮中心指揮官陳時中早在7月12日就宣布，若沒其他疫苗可選，BNT疫苗就會保留給學生先打。\n不過，BNT疫苗要開打在12到18歲的青少年族群，還差一關，就是得先向食藥署申請緊急使用授權（EUA）的變更適用適應症，相關程序才算真正到位。\n吳秀梅表示，針對這一點，食藥署已經有個別向鴻海及台積電提醒他們了，只不過兩家企業申請購買疫苗時，國外的臨床實驗還在做，但現在要變更適應症並不困難，只要兩家企業接洽的上海復星提審書面資料，就算在疫苗快到之前 再做申請，一樣來得及。\n至於送件之後是否還需要開專家會議？吳秀梅強調，這不是必要過程，食藥署若審核書面資料「我們看適合就可以核准」，畢竟國外已有臨床試驗數字，加上已有些地方已經開始在打12到18歲族群了，不一定要另開專家會議，除非有需要專家再提供意見的地方。\n隨後指揮中心則指出，相關變更會由疾管署做專案申請，專案申請會將12到18歲的緊急使用納入申請內容，請民眾放心。\n照片來源：資料照\n更多匯流新聞網報導：\n全台508處失智社區服務據點解封條件出爐！ 最快8月恢復服務\n6旬婦發病到死亡僅2天！ 羅一鈞揭長期臥床「查無接觸史」引關注\n【文章轉載請註明出處】\n \n\n",
        keywords=["BNT疫苗", "適應症", "青少年"],
        category=None,
        media="匯流新聞網",
        datetime="\n\n2021-07-20\n",
        link="https://cnews.com.tw/003210720a10/",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return cnews.CNewsNewsCrawler()


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
