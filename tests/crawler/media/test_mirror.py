# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from src.crawler.media import mirror
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
    name="鏡週刊_1",
    link="https://www.mirrormedia.mg/story/20210409money006/",
    expected_output=NewsStruct(
        title="【官股投資術2】台股萬六害怕股災來臨　達人：官股超抗跌這3檔必買",
        content="官股股性穩健安全，除了不少大到不會倒的官股金融股，例如兆豐金、合庫金、第一金等，另外像是台汽電（8926）、中再保（2851）等，歷年平均殖利率皆有逾6%，存股達人股魚就表示，不少官股屬於獨佔事業，遇到股災來時，相對於其他個股，股價更穩定。\n財經部落客股魚表示，許多官股企業早期都屬於獨佔壟斷產業，例如中華電，電纜光纖一家獨大，欣字輩如欣高、欣泰、欣雄等都是供應天然氣，依照供給天然氣區域不同，名稱各異，皆為官股持有的天然氣公司，對於追求穩定的投資人來說，是個合適的存股標的。\n「遇到股災的時候，相對於其他個股，官股的股價也較穩定。」而多檔官股，股魚最推薦跟景氣波動關聯低的股票，特別點名以下3檔，供投資人參考。\n一、類台股債券－中華電\n「中華電（2412）類似台股的債券，股災來抗跌，大盤漲也不漲，但每年殖利率大約5%。」股魚表示，如果投資人買官股，前提是為穩定領現金股利，那中華電是不錯的選擇。相較去年3月股災時，台股大盤下跌近3成，但中華電僅跌6.4%，確實是最佳抗跌股。\n二、天然氣壟斷事業－欣泰\n退輔會持股24.6%的欣泰天然瓦斯，主要供應北部天然氣，穩定性高，在北部地區接近壟斷企業，是天然氣獨家供應者。\n三、進出口報關事業－關貿\n關貿主要從事進出口報關，以及財政部的交易網絡等，例如民眾在淘寶上購物，進出海關進行實名申報，或是報稅系統等都是關貿開發，「只要是與財政部扯上關係，以及與財政部金流管理的後面廠商都是關貿。因此，穩定度和獲利都很不錯。」股魚分析。\n只是官股獲利穩定，但難有「爆發性成長」，例如台鹽（1737），早期主要獲利來源是販賣食用鹽，但隨著產業轉型，後來朝生技美妝發展，「由於是官股，操作上非常保守，賺錢能力不是很強。」不過轉型後每一年都有持續獲利，配息亦穩定。\n此外，中央再保險公司，簡稱中再保（2851），鮮少人知道中再保存在，其實中再保歷年平均殖利率皆有6%以上水準，其業務有6至7成為產險，其餘是壽險。與一般保險公司不同之處，中再保的客戶為保險公司，等於是保險公司再分攤風險用的一間保險公司，保險公司的保險公司。\n\n    更多內容，歡迎訂閱鏡週刊、了解內容授權資訊。\n  ",
        keywords=["官股", "股魚", "台汽電", "中再保", "殖利率", "兆豐金", "第一金控"],
        category="財經理財",
        media="鏡週刊",
        datetime="2021-04-09T21:58:57.000Z",
        link="https://www.mirrormedia.mg/story/20210409money006/",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="鏡週刊_2",
    link="https://www.mirrormedia.mg/story/20210409money005/",
    expected_output=NewsStruct(
        title="【官股投資術1】政府掛保證達人也愛　他大買這檔100張爽領9%殖利率",
        content="隨著台股續創新高、邁向萬七大關，投資人不免心驚驚，指數狂飆之際，該如何選股才能買得放心、抱得安心？擁有政府當靠山的官股突顯其「穩健、安全」的價值，不論是眾人熟知的中華電、台汽電、兆豐金、合庫金等，現金殖利率都維持在5～6%，是定存的6倍。\n存股達人算利教官楊禮軒握有台汽電（8926）14年，看準的就是官股穩定配息，他從股價20元開始買進，一路加碼至100張，「光今年配息1.9元，以我買進成本而言，相當於殖利率9.5%，光今年就貢獻約19萬現金股息。」楊禮軒說。\n他進一步分享，這些年長期持有台汽電，價差早已翻倍，以買進價格計算，每年領取股息、換算殖利率在6～9.5%之間。除了敲進成本夠低，他抱緊台汽電的很大原因是，「這個產業不受景氣循環影響，政府廢核減媒對台汽電都有正面的助益。」楊禮軒說，相較民營企業，台汽電股東有3成官股，公司治理循規蹈矩，穩妥安定是一大關鍵因素。\n除了台汽電，算利教官分享，手中持有另一檔官股欣泰（8917），欣泰主要營業項目為天然氣銷售及供氣管線安裝，屬民營公用事業、官股占24.6%。「退輔會是大股東，但是我喜歡它屬民生必需類股、不受景氣循環影響。」他坦言，從去年初開始買進欣泰，成本約50元，「參與配息配股，每張變成1.1張，換算目前市值，不到一年成長超過66%。」\n楊禮軒進一步說明，2020年7月政府實施的鍋爐管制規定，欣泰所在區域的工廠燃煤跟重油鍋爐，紛紛改為天然氣鍋爐，使營收持續成長，經營區內都更案跟建案，推升更多天然瓦斯申裝與使用\n加上民營公用事業管制規定在2019年廢止後，欣泰再也不用受到規定獲利超過股本25%要繳回的限制，營運自由度大幅提升。算利教官表示，官股背景的公司，得配合政府政策，較難「與民爭利」，但若經營實績佳，都可以為投資人帶來穩定獲利。\n台汽電（8926）近5年表現\n\n    更多內容，歡迎訂閱鏡週刊、了解內容授權資訊。\n  ",
        keywords=["存股", "楊禮軒", "台汽電", "中華電", "兆豐金", "合庫", "殖利率", "台股"],
        category="財經理財",
        media="鏡週刊",
        datetime="2021-04-09T21:58:58.000Z",
        link="https://www.mirrormedia.mg/story/20210409money005/",
    ),
)


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return mirror.MirrorNewsCrawler()


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
