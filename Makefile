export PYTHONPATH=./

run_sample_yahoo:
	python src/media/entry.py \
		-m yahoo \
		-l \
		https://tw.stock.yahoo.com/news/%E7%86%B1%E9%96%80%E6%97%8F%E7%BE%A4-%E5%A7%94%E5%A4%96%E8%A8%82%E5%96%AE%E6%97%BA-%E5%89%B5%E6%84%8F%E5%8A%9B%E6%97%BA%E6%A5%AD%E7%B8%BE%E8%A3%9C-234511435.html \
		https://tw.news.yahoo.com/%E5%85%AC%E5%8F%B8%E6%B2%BB%E7%90%86100%E6%8C%87%E6%95%B8-%E6%88%90%E5%88%86%E8%82%A1%E6%96%B0%E5%A2%9E32%E6%AA%94-115754553.html \
		-o out/sample_yahoo.json \

run_sample_ettoday:
	python src/media/entry.py \
	-m ettoday \
	-l \
	https://www.ettoday.net/news/20210720/2035771.htm \
	https://finance.ettoday.net/news/1929335 \
	-o out/sample_ettoday.json \

run_sample_ltn:
	python src/media/entry.py \
	-m ltn \
	-l \
	https://news.ltn.com.tw/news/business/breakingnews/3604805 \
	https://ec.ltn.com.tw/article/breakingnews/3468538 \
	-o out/sample_ltn.json \

run_sample_chinatimes:
	python src/media/entry.py \
	-m chinatimes \
	-l \
	https://www.chinatimes.com/realtimenews/20210712002325-260410 \
	https://www.chinatimes.com/realtimenews/20210428001632-260410 \
	-o out/sample_chinatimes.json \

run_sample_udn:
	python src/media/entry.py \
	-m udn \
	-l \
	https://udn.com/news/story/7253/5550651 \
	https://udn.com/news/story/7254/5542521 \
	-o out/sample_udn.json \

## NO NEWS
# run_sample_ttv:
# 	python src/media/entry.py \
# 	-m ttv \
# 	-l \

# 	-o out/sample_ttv.json \

run_sample_ftv:
	python src/media/entry.py \
	-m ftv \
	-l \
	https://www.ftvnews.com.tw/news/detail/2021713W0276 \
	https://www.ftvnews.com.tw/news/detail/2021721W0079 \
	-o out/sample_ftv.json \

## NO NEWS
# run_sample_cts:
# 	python src/media/entry.py \
# 	-m cts \
# 	-l \

# 	-o out/sample_cts.json \

run_sample_sina:
	python src/media/entry.py \
	-m sina \
	-l \
	https://news.sina.com.tw/article/20210318/37931108.html \
	https://news.sina.com.tw/article/20210415/38230928.html \
	-o out/sample_sina.json \

run_sample_appledaily:
	python src/media/entry.py \
	-m appledaily \
	-l \
	https://tw.appledaily.com/property/20210722/X7R2YYQTSJA3FMCB642SBQY5JM/ \
	https://tw.appledaily.com/property/20200616/TYDZD67VFHQM3PKCZDL6ZL4TCA/ \
	-o out/sample_appledaily.json \

run_sample_moneyudn:
	python src/media/entry.py \
	-m moneyudn \
	-l \
	https://money.udn.com/money/story/5607/5047950 \
	https://money.udn.com/money/story/5612/5560454 \
	-o out/sample_moneyudn.json \

run_sample_ctee:
	python src/media/entry.py \
	-m ctee \
	-l \
	https://ctee.com.tw/news/stocks/491412.html \
	https://ctee.com.tw/news/stocks/487126.html \
	-o out/sample_ctee.json \

## no script_info
# run_sample_technews:
# 	python src/media/entry.py \
# 	-m technews \
# 	-l \
# 	https://finance.technews.tw/2021/06/09/caswell-6416-202105-financial-report/ \
# 	https://finance.technews.tw/2021/07/09/mvi-2342-202106-financial-report/ \
# 	-o out/sample_technews.json \

run_sample_bnext:
	python src/media/entry.py \
	-m bnext \
	-l \
	https://meet.bnext.com.tw/articles/view/44652 \
	-o out/sample_bnext.json \

run_sample_cynes:
	python src/media/entry.py \
	-m cynes \
	-l \
	https://news.cnyes.com/news/id/4520040 \
	https://m.cnyes.com/news/id/4537458 \
	-o out/sample_cynes.json \

## bs4 cannot catch content
run_sample_ebc:
	python src/media/entry.py \
	-m ebc \
	-l \
	https://fnc.ebc.net.tw/FncNews/stock/127025 \
	https://fnc.ebc.net.tw/fncnews/else/135466 \
	-o out/sample_ebc.json \
