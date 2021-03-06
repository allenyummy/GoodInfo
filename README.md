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
            stock_code = d["????????????"]
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
            ????????? 2330
            ????????? 2454
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
        results = gnc.getInfo(query="????????? 2330")
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
            |  appledaily |    o       | [????????????](https://tw.appledaily.com) 
            |   bcc       |    o       | [??????????????????](https://www.bcc.com.tw)
            |   bnext     |    o       | [????????????](https://www.bnext.com.tw) <br> [Meet????????????](https://meet.bnext.com.tw)
            |  chinatimes |    o       | [???????????????](https://www.chinatimes.com)
            |   cmmedia   |    o       | [?????????](https://www.cmmedia.com.tw)
            |   cna       |    o       | [?????????](https://www.cna.com.tw)
            |   cnews     |    o       | [???????????????](https://cnews.com.tw)
            |   ctee      |    o       | [????????????](https://ctee.com.tw)
            |   ctitv     |    o       | [????????????](https://gotv.ctitv.com.tw)
            |   cts       |    o       |  [????????????](https://news.cts.com.tw)
            |   ctv       |    x <br> (audio-visual) | [????????????](http://new.ctv.com.tw)
            |   cynes     |    o       |  [?????????](https://m.cnyes.com) <br> [???????????????](https://news.cnyes.com)
            |   digitimes |    o       |  [DigiTimes](https://www.digitimes.com.tw)
            |   ebc       |    x <br> (contents are locked) | [??????????????????](https://fnc.ebc.net.tw)
            |  epochtimes |    o       | [?????????](https://www.epochtimes.com)
            |   era       |    o       | [????????????](https://www.eracom.com.tw)
            |   ettoday   |    o       | [ETtoday?????????](https://www.ettoday.net) <br> [ETtoday?????????](https://finance.ettoday.net)
            |   ftv       |    o       | [????????????](https://www.ftvnews.com.tw)
            |   kairos    |    o       | [????????????](https://kairos.news)
            |   ltn       |    o       | [?????????????????????](https://news.ltn.com.tw) <br> [????????????](https://ec.ltn.com.tw)
            |   mirror    |    o       | [?????????](https://www.mirrormedia.mg)
            |   moneydj   |    o       | [MoneyDJ?????????](https://www.moneydj.com)
            |   moneyudn  |    o       | [????????????](https://money.udn.com)
            | mypeoplevol |    o       | [???????????????](https://www.mypeoplevol.com)
            |   newtalk   |    o       | [?????????](https://newtalk.tw)
            |   nownews   |    o       | [????????????](https://www.nownews.com)
            |   pchome    |    o       | [PChome??????](https://news.pchome.com.tw)
            |  peoplenews |    o       | [??????](https://www.peoplenews.tw)
            |   pts       |    o       | [????????????](https://news.pts.org.tw)
            |   rti       |    o       | [??????????????????](https://www.rti.org.tw)
            |   setn      |    o       | [????????????](https://www.setn.com)
            |   sina      |    o       | [????????????](https://news.sina.com.tw)
            |   storm     |    o       | [?????????](https://www.storm.mg)
            |   taiwanhot |    o       | [???????????????](http://www.taiwanhot.net)
            |   taronews  |    o       | [?????????](https://taronews.tw)
            |   technews  |    o       | [????????????](https://technews.tw) <br> [????????????](https://finance.technews.tw)
            | thenewslens |    o       | [???????????????](https://www.thenewslens.com) 
            |   ttv       |    o       | [????????????](https://news.ttv.com.tw)
            |   tvbs      |    o       | [TVBS](https://news.tvbs.com.tw)
            |   udn       |    o       | [???????????????](https://udn.com)
            |   upmedia   |    o       | [??????](https://www.upmedia.mg)
            |   ustv      |    o       | [????????????](https://news.ustv.com.tw)
            |   wealth    |    o       | [??????](https://www.wealth.com.tw)
            | worldjournal|    o       | [???????????????](https://www.worldjournal.com)
            |   yahoo     |    o       | [Yahoo????????????](https://tw.news.yahoo.com) <br> [Yahoo????????????](https://tw.stock.yahoo.com)


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
