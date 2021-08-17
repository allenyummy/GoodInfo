.PHONY: clean

clean:
	find . -name '.pytest_cache' -type d -exec rm -rf {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +

export PYTHONPATH=./


####################################################
####################### HELP #######################
####################################################

help:
	@echo "usage: make [command] [arguments=xxx]"
	@echo " "
	@echo "[command]"
	@echo "   run_sample     : Run sample of specific media"
	@echo "   run_sample_all : Run sample of all media which are listed below"
	@echo "   run_test       : Run test of specific test"
	@echo "   run_test_all   : Run test of all media which are listed below"
	@echo " "
	@echo "[arguments]"
	@echo "   media          : Select target media as input."
	@echo "                    The argument is only used by run_command and run_test."
	@echo "                    The supported media options are as follows:"
	@echo "                          yahoo ettoday ltn chinatimes udn"
	@echo "                          ftv sina appledaily moneyudn ctee"
	@echo "                          bnext cynes ttv cts technews ebc"
	@echo "                          cmmedia storm mirror cna bcc wealth"
	@echo "                          digitimes moneydj cnews ctitv ctv"
	@echo "                          epochtimes era kairos mypeoplevol"
	@echo "                          newtalk nownews pchome peoplenews"
	@echo "                          pts rti setn taiwanhot taronews"
	@echo "                          thenewslens tvbs upmedia ustv worldjournal"


####################################################
####### VARIABLEs of run_sample and run_test #######
####################################################

## MEDIA
TARGET_MEDIA = yahoo ettoday ltn chinatimes udn \
               ftv sina appledaily moneyudn ctee \
               bnext cynes ttv cts technews ebc \
               cmmedia storm mirror cna bcc wealth \
               digitimes moneydj cnews ctitv ctv \
               epochtimes era kairos mypeoplevol \
               newtalk nownews pchome peoplenews \
               pts rti setn taiwanhot taronews \
               thenewslens tvbs upmedia ustv worldjournal


## SAMPLE LINK
sample_yahoo_link        = "https://tw.stock.yahoo.com/news/%E7%86%B1%E9%96%80%E6%97%8F%E7%BE%A4-%E5%A7%94%E5%A4%96%E8%A8%82%E5%96%AE%E6%97%BA-%E5%89%B5%E6%84%8F%E5%8A%9B%E6%97%BA%E6%A5%AD%E7%B8%BE%E8%A3%9C-234511435.html" \
                           "https://tw.news.yahoo.com/%E5%85%AC%E5%8F%B8%E6%B2%BB%E7%90%86100%E6%8C%87%E6%95%B8-%E6%88%90%E5%88%86%E8%82%A1%E6%96%B0%E5%A2%9E32%E6%AA%94-115754553.html"
sample_ettoday_link      = "https://www.ettoday.net/news/20210720/2035771.htm" \
                           "https://finance.ettoday.net/news/1929335"
sample_ltn_link          = "https://news.ltn.com.tw/news/business/breakingnews/3604805" \
                           "https://ec.ltn.com.tw/article/breakingnews/3468538"
sample_chinatimes_link   = "https://www.chinatimes.com/realtimenews/20210712002325-260410" \
                           "https://www.chinatimes.com/realtimenews/20210428001632-260410"
sample_udn_link          = "https://udn.com/news/story/7253/5550651" \
                           "https://udn.com/news/story/7254/5542521"
sample_ttv_link          = "https://news.ttv.com.tw/news/11008170000600W" \
                           "https://news.ttv.com.tw/news/11008170002600W"
sample_ftv_link          = "https://www.ftvnews.com.tw/news/detail/2021713W0276" \
                           "https://www.ftvnews.com.tw/news/detail/2021721W0079"
sample_cts_link          = "https://news.cts.com.tw/cts/money/202108/202108162053145.html" \
                           "https://news.cts.com.tw/cts/money/202107/202107282051061.html"
sample_sina_link         = "https://news.sina.com.tw/article/20210318/37931108.html" \
                           "https://news.sina.com.tw/article/20210415/38230928.html"
sample_appledaily_link   = "https://tw.appledaily.com/property/20210722/X7R2YYQTSJA3FMCB642SBQY5JM/" \
                           "https://tw.appledaily.com/property/20200616/TYDZD67VFHQM3PKCZDL6ZL4TCA/"
sample_moneyudn_link     = "https://money.udn.com/money/story/5607/5047950" \
                           "https://money.udn.com/money/story/5612/5560454"
sample_ctee_link         = "https://ctee.com.tw/news/stocks/491412.html" \
                           "https://ctee.com.tw/news/stocks/487126.html"
sample_technews_link     = "https://finance.technews.tw/2021/06/09/caswell-6416-202105-financial-report/" \
                           "https://finance.technews.tw/2021/07/09/mvi-2342-202106-financial-report/"
sample_bnext_link        = "https://meet.bnext.com.tw/articles/view/44652" \
                           "https://meet.bnext.com.tw/articles/view/47657"
sample_cynes_link        = "https://news.cnyes.com/news/id/4520040" \
                           "https://m.cnyes.com/news/id/4537458"
sample_ebc_link          = "https://fnc.ebc.net.tw/FncNews/stock/127025" \
                           "https://fnc.ebc.net.tw/fncnews/else/135466"
sample_cmmedia_link      = "https://www.cmmedia.com.tw/home/articles/28422" \
                           "https://www.cmmedia.com.tw/home/articles/29234"
sample_storm_link        = "https://www.storm.mg/article/3018203" \
                           "https://www.storm.mg/lifestyle/3578464"
sample_mirror_link       = "https://www.mirrormedia.mg/story/20210409money006/" \
                           "https://www.mirrormedia.mg/story/20210409money005/"
sample_cna_link          = "https://www.cna.com.tw/news/afe/202107200398.aspx" \
                           "https://www.cna.com.tw/news/afe/202108110212.aspx"
sample_bcc_link          = "https://www.bcc.com.tw/newsView.6473942" \
                           "https://www.bcc.com.tw/newsView.4839712"
sample_wealth_link       = "https://www.wealth.com.tw/home/articles/31815" \
                           "https://www.wealth.com.tw/home/articles/32190"
sample_digitimes_link    = "https://www.digitimes.com.tw/iot/article.asp?cat=130&cat1=40&cat2=13&id=0000613290_cby1uhlilg4hjclrwlpe5" \
                           "https://www.digitimes.com.tw/iot/article.asp?cat=158&cat1=20&cat2=&id=0000616397_OKT27NZLLU5LRU60OSZYT"
sample_moneydj_link      = "https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6f1bfd5e-30bb-4fcf-b7ee-4fcb0c19696e" \
                           "https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6c236fc2-97e0-4676-9846-a4d45c9ec199"
sample_cnews_link        = "https://cnews.com.tw/209210813a01/" \
                           "https://cnews.com.tw/003210720a10/"
sample_ctitv_link        = "https://gotv.ctitv.com.tw/2021/08/1855737.htm" \
                          "https://gotv.ctitv.com.tw/2021/08/1855470.htm"
sample_ctv_link          =
sample_epochtimes_link   = "https://www.epochtimes.com/b5/21/8/15/n13163638.htm" \
                           "https://www.epochtimes.com/b5/21/8/10/n13153632.htm"
sample_era_link          = "https://www.eracom.com.tw/EraNews/Home/Entertainment/2021-08-17/544662.html" \
                           "https://www.eracom.com.tw/EraNews/Home/Finance/2021-08-16/544573.html"
sample_kairos_link       = "https://kairos.news/350866" \
                           "https://kairos.news/368246"
sample_mypeoplevol_link  = "https://www.mypeoplevol.com/Article/3493" \
                           "https://www.mypeoplevol.com/Article/3485"
sample_newtalk_link      = "https://newtalk.tw/news/view/2021-08-13/620248" \
                           "https://newtalk.tw/news/view/2021-08-11/619072"
sample_nownews_link      = "https://www.nownews.com/news/5357780" \
                           "https://www.nownews.com/news/5357268"
sample_pchome_link       = "https://news.pchome.com.tw/finance/cna/20210817/index-16291636203632218003.html" \
                           "https://news.pchome.com.tw/finance/cna/20210817/index-16291653018707918003.html"
sample_peoplenews_link   = "https://www.peoplenews.tw/news/43062927-5349-4606-b18f-e673004c6c88" \
                           "https://www.peoplenews.tw/news/ece2d1ae-a4b7-489b-b382-afe1e1da93d0"
sample_pts_link          = "https://news.pts.org.tw/article/540373"\
                           "https://news.pts.org.tw/article/540195"
sample_rti_link          = "https://www.rti.org.tw/news/view/id/2108692" \
                           "https://www.rti.org.tw/news/view/id/2108706"
sample_setn_link         = "https://www.setn.com/News.aspx?NewsID=981898" \
                           "https://www.setn.com/News.aspx?NewsID=983646"
sample_taiwanhot_link    = "https://www.taiwanhot.net/?p=957639" \
                           "https://www.taiwanhot.net/?p=957645"
sample_taronews_link     = "https://taronews.tw/2021/08/17/771295" \
                           "https://taronews.tw/2021/08/17/771237"
sample_thenewslens_link  = "https://www.thenewslens.com/article/155125" \
                           "https://www.thenewslens.com/article/155123"
sample_tvbs_link         = "https://news.tvbs.com.tw/money/1566997" \
                           "https://news.tvbs.com.tw/politics/1567072"
sample_upmedia_link      = "https://www.upmedia.mg/news_info.php?SerialNo=121668" \
                           "https://www.upmedia.mg/news_info.php?SerialNo=121781"
sample_ustv_link         = "https://news.ustv.com.tw/newsdetail/20210816A001044?type=147&" \
                           "https://news.ustv.com.tw/newsdetail/20210816A098?type=144&listOnly=true"
sample_worldjournal_link = "https://www.worldjournal.com/wj/story/121347/5679553?from=wj_catelistnews" \
                           "https://www.worldjournal.com/wj/story/121218/5679359?from=wj_catebreaknews"

####################################################
###################### TASKs #######################
####################################################

TASKS = run_sample run_sample_all run_test run_test_all
.PHONY: $(TASKS)

run_sample:
ifeq ($(media), $(filter $(media), $(TARGET_MEDIA)))
	python src/entry_media.py \
		-m $(media) \
		-l $(sample_$(media)_link) \
		-o out/sample_$(media).json
else
	@echo "make run_sample media=$(media)"
	@echo "   media only supports the following arguments:"
	@echo "      $(TARGET_MEDIA)"
	@echo "   but got media=$(media)."
endif

run_sample_all:
	for media in $(TARGET_MEDIA); do \
		echo ====== $$media ======; \
		make run_sample media=$$media; \
	done

run_test:
ifeq ($(media), $(filter $(media), $(TARGET_MEDIA)))
	pytest tests/test_crawler_media/test_$(media).py \
		--log-cli-level=warning \
		--cov=./ \
		--cov-report term-missing
else
	@echo "make run_test media=$(media)"
	@echo "   media only supports the following arguments:"
	@echo "      $(TARGET_MEDIA)"
	@echo "   but got media=$(media)."
endif

run_test_all:
	pytest tests/ \
		--log-cli-level=warning \
		--cov=./ \
		--cov-report term-missing

# run_test_all:
# for media in $(TARGET_MEDIA); do \
# 	echo ====== $$media ======; \
# 	make run_test media=$$media; \
# done
