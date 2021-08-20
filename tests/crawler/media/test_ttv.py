# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import ttv
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
    name="台視新聞_1",
    link="https://news.ttv.com.tw/news/11008170000600W",
    expected_output=NewsStruct(
        title="聯亞藥早盤重挫逾50% 高端亮燈漲停",
        content="\n指揮中心16日宣布，聯亞疫苗EUA審核未通過，導致子公司聯亞藥昨日股價狂瀉，今（17）日開盤再度重挫，報116元，早盤跌幅一度超過50%，最低至82元，盤中拉回百元之上。昨日衝上漲停的高端疫苗，今日維持漲勢，開盤報348元，漲幅持續擴大，10點15分後已大漲超過9%，在10點51分亮燈漲停。責任編輯／林湘芸\n",
        keywords=["聯亞藥", "高端疫苗", "台股", "股價", "EUA", "財經"],
        category="財經",
        media="台視新聞",
        datetime="2021-08-17T10:35:15+08:00",
        link="https://news.ttv.com.tw/news/11008170000600W",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="台視新聞_2",
    link="https://news.ttv.com.tw/news/11008170002600W",
    expected_output=NewsStruct(
        title="賴清德登記高端疫苗！ 等候預約通知",
        content="\n副總統賴清德原本預計要接種國產聯亞疫苗，不過因聯亞申請緊急使用授權EUA未通過，他昨天表示將改接種高端疫苗，今天中午就透過臉書表示，「今天上午，我已經上網完成國產高端疫苗接種意願登記」，等待指揮中心通知預約，完成疫苗接種，他和國人一起團結防疫守台灣。賴清德也請符合資格的國人，儘速登記預約接種，大家一起提升群體免疫力，取得對病毒的抵抗力，保護自己的健康。賴副總統並說，他也要拜託大家，繼續落實防疫措施，遵守各場所防疫指引，全民共同努力，早日回到正常生活。責任編輯／林均\n",
        keywords=["賴清德", "高端疫苗", "疫苗預約平台", "登記", "疫苗", "生活", "副總統", "政治"],
        category="政治",
        media="台視新聞",
        datetime="2021-08-17T15:17:19+08:00",
        link="https://news.ttv.com.tw/news/11008170002600W",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ttv.TTVNewsCrawler()


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
