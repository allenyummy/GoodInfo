# Web Crawler for GoodInfo and Financial News of Companies in Taiwan

It's a web crawler to get information of listed companies, including their english names, chinese names, abbreviation, codes, and important related people. Besides, it also gets news of these companies. My goal is to build up a dataset of financial news to help the development of Chinese Natural Language Processing.

---

## Prepare virtual environment
```
$ conda create --name GoodInfo-py38 python=3.8
$ conda activate GoodInfo-py38
$ git clone https://github.com/allenyummy/GoodInfo.git
```

### Install basic dependencies

If just use the repo as a service, it's enough to only install basic dependencies.
There are two ways to achieve the goal.

+ Run commands with `poetry install`
    ```
    $ pip install poetry
    $ poetry install --no-dev
    ```

+ Run commands with `pip install`
    ```
    $ pip install -r requirements.txt
    ```

### Install basic and dev dependencies (optional)
If wanna modify some codes, it's highly recommended to install both basic and dev dependencies.

+ Run command with `poetry install`
    ```
    $ pip install poetry
    $ poetry install
    $ pre-commit install
    ```

---

## Run Code

### Set uo
Run below command to make sure there is "./" dir in PYTHONPATH.
```
$ export PYTHONPATH=./
```
After doing this, make sure working directory is `xxx/GoodInfo/`.

### Get company info

+ Get entire basic information
    + Run with command line interface
        ```
        $ python src/entry_goodinfo.py \
            -o $(outfile).json \
            -c $(cachefile).json
        ```
        Noted:
        + Caution

            GoodInfo may recognize the program as automated robots and block the IP; therefore, <b><u>connect hotspot from iphone</u></b> to run the program. Once your IP address is blocked by Google, you can turn on flight mode and then turn off, and re-open your hotspot to change your IP address (p.s., hotspot ip address is floating.).

    + Run with python package
        ```
        from src.crawler.goodinfo.goodinfo import get_code_name, get_basic

        data = get_code_name()
        for d in data:
            stock_code = d["股票代號"]
            d_basic = get_basic(stock_code)
        ```

### Get google news info

+ Get google news

    + Run with command line interface
        ```
        $ python src/crawler/googlenews/gnews.py \
            -iq $(input_query_file).txt \
            -o $(outfile).json \
            -c $(cachefile).json \
        ```
        Noted:

        + `$(input_query_file).txt` contains queries for `src/crawler/googlenews/gnews.py`. One query per line and if a query contains multiple keywords, keywords should be concatenated with space. For example:
            ```
            台積電 2330
            聯發科 2454
            ...
            ```
        + `$(outfile)` and `$(cachefile)` could be same or different. Both of them must be json file.
        + The results should contain <b>title</b>, <b>description</b>, <b>media</b>, <b>datetime</b>, <b>link</b>. See more details in `src/utils/struct::GoogleNewsStruct`.
        + Caution

            Google may recognize the program as automated robots and block the IP, using cloud server and fetching data with high frequency will get higher chance to be blocked. Therefore, <b><u>connect hotspot from iphone</u></b> to run `gnews.py`. Once your IP address is blocked by Google, you can turn on flight mode and then turn off, and re-open your hotspot to change your IP address (p.s., hotspot ip address is floating.). Besides, I use `time.sleep(random.uniform(30, 50))` but it may lower the possibility to get IP blocked.

            If got locked, you'll receive a message of `HTTP Error 420: Too many requests`. Just do the action mentioned above and you can run the program successfully.

    + Run with python package
        ```
        from src.crawler.googlenews.gnews import GoogleNewsCrawler

        gnc = GoogleNewsCrawler()
        results = gnc.getInfo(query="台積電 2330")
        ```

### Get news (given a link or links)

+ Get news details

    + Run with command line interface
        ```
        $ python src/entry_media.py \
            -m $(media) \
            -l $(link) \
            -o $(outfile).json \
            -c $(cachefile).json \
        ```
        Noted:

        + `$(link)` could be one or multiple. If multiple links, spearated them by white space.
        + `$(outfile)` and `$(cachefile)` could be same or different. Both of them must be json file.
        + The results should contain <b>title</b>, <b>content</b>, <b>keywords</b>, <b>category</b>, <b>media</b>, <b>datetime</b>, <b>link</b>. See more details in `src/utils/struct::NewsStruct`.
        + `$(media)` args could be as follows:

            |    media    |  supported |  main url   |
            |:-----------:|:----------:|:-----------:|
            |  appledaily |    o       | [蘋果日報](https://tw.appledaily.com) 
            |   bcc       |    o       | [中國廣播公司](https://www.bcc.com.tw)
            |   bnext     |    o       | [數位時代](https://www.bnext.com.tw) <br> [Meet創業小聚](https://meet.bnext.com.tw)
            |  chinatimes |    o       | [中時新聞網](https://www.chinatimes.com)
            |   cmmedia   |    o       | [信傳媒](https://www.cmmedia.com.tw)
            |   cna       |    o       | [中央社](https://www.cna.com.tw)
            |   cnews     |    o       | [匯流新聞網](https://cnews.com.tw)
            |   ctee      |    o       | [工商時報](https://ctee.com.tw)
            |   ctitv     |    o       | [中天新聞](https://gotv.ctitv.com.tw)
            |   cts       |    o       |  [華視新聞](https://news.cts.com.tw)
            |   ctv       |    x <br> (audio-visual) | [中視新聞](http://new.ctv.com.tw)
            |   cynes     |    o       |  [鉅亨網](https://m.cnyes.com) <br> [鉅亨新聞網](https://news.cnyes.com)
            |   digitimes |    o       |  [DigiTimes](https://www.digitimes.com.tw)
            |   ebc       |    x <br> (contents are locked) | [東森財經新聞](https://fnc.ebc.net.tw)
            |  epochtimes |    o       | [大紀元](https://www.epochtimes.com)
            |   era       |    o       | [年代新聞](https://www.eracom.com.tw)
            |   ettoday   |    o       | [ETtoday新聞雲](https://www.ettoday.net) <br> [ETtoday財經雲](https://finance.ettoday.net)
            |   ftv       |    o       | [民視新聞](https://www.ftvnews.com.tw)
            |   kairos    |    o       | [風向新聞](https://kairos.news)
            |   ltn       |    o       | [自由時報電子報](https://news.ltn.com.tw) <br> [自由財經](https://ec.ltn.com.tw)
            |   mirror    |    o       | [鏡週刊](https://www.mirrormedia.mg)
            |   moneydj   |    o       | [MoneyDJ理財網](https://www.moneydj.com)
            |   moneyudn  |    o       | [經濟日報](https://money.udn.com)
            | mypeoplevol |    o       | [民眾新聞網](https://www.mypeoplevol.com)
            |   newtalk   |    o       | [新頭殼](https://newtalk.tw)
            |   nownews   |    o       | [今日新聞](https://www.nownews.com)
            |   pchome    |    o       | [PChome新聞](https://news.pchome.com.tw)
            |  peoplenews |    o       | [民報](https://www.peoplenews.tw)
            |   pts       |    o       | [公視新聞](https://news.pts.org.tw)
            |   rti       |    o       | [中央廣播電臺](https://www.rti.org.tw)
            |   setn      |    o       | [三立新聞](https://www.setn.com)
            |   sina      |    o       | [新浪新聞](https://news.sina.com.tw)
            |   storm     |    o       | [風傳媒](https://www.storm.mg)
            |   taiwanhot |    o       | [台灣好新聞](http://www.taiwanhot.net)
            |   taronews  |    o       | [芋傳媒](https://taronews.tw)
            |   technews  |    o       | [科技新報](https://technews.tw) <br> [財經新報](https://finance.technews.tw)
            | thenewslens |    o       | [關鍵評論網](https://www.thenewslens.com) 
            |   ttv       |    o       | [台視新聞](https://news.ttv.com.tw)
            |   tvbs      |    o       | [TVBS](https://news.tvbs.com.tw)
            |   udn       |    o       | [聯合新聞網](https://udn.com)
            |   upmedia   |    o       | [上報](https://www.upmedia.mg)
            |   ustv      |    o       | [非凡新聞](https://news.ustv.com.tw)
            |   wealth    |    o       | [財訊](https://www.wealth.com.tw)
            | worldjournal|    o       | [世界新聞網](https://www.worldjournal.com)
            |   yahoo     |    o       | [Yahoo奇摩新聞](https://tw.news.yahoo.com) <br> [Yahoo奇摩股市](https://tw.stock.yahoo.com)


        + run example code for specific media, and it will generate a `out/sample_$(media).json` in local.
            ```
            $ make run_example media=$(media)
            ```
    
    + Run with python package
        ```
        from src.crawler.media.factory import MediaNewsCrawlerFactory
        
        nc = MediaNewsCrawlerFactory(media_name="appledaily")
        result = nc.getInfo(link="xxxxxx")
        ```

---

## Test

+ Test media crawler
    ```
    $ make run_test_all
    ```
