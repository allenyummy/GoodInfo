# Web Crawler for GoodInfo and Financial News of Companies in Taiwan

It's a web crawler to get information of listed companies, including their english names, chinese names, abbreviation, codes, and important related people. Besides, it also gets news of these companies. My goal is to build up a dataset of financial news to help the development of Chinese Natural Language Processing.

---

## Prepare virtual environment
```
$ conda create --name GoodInfo-py38 python=3.8
$ conda activate GoodInfo-py38
$ git clone https://github.com/allenyummy/GoodInfo.git
$ export PYTHONPATH=./
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

## Run code

### Get company info

+ Only get code and name to `out/company.json`
    ```
    $ python main.py -g1 -o out/company.json
    ```

+ Get entire basic information to `out/company.json`
    ```
    $ python main.py -g1 -g2 -o out/company.json
    ```

+ Your ip address may be locked, so you can use it to restart your progam to get the rest basic information
    ```
    $ python main.py -g2 -c out/company.json -o out/company.json
    ```

### Get google news info

+ Get google news. (I've not written argsparse yet. Sorry for inconvenience.)
    ```
    PYTHONPATH=./ python src/gnews.json
    ```
    Noted that you should run above code to get `out/company.json`
    Also, I use `time.sleep(30)` but it still got locked when get news every 40 companies, so I terminate the code every 40 companies to avoid your IP address locked.

### Get news (given a link or links)

+ Get news details (<b>title</b>, <b>content</b>, <b>keywords</b>, <b>category</b>, <b>media</b>, <b>datetime</b>, <b>link</b>)
    ```
    python src/entry_media.py \
        -m $(media) \
        -l $(link) \
        -o $(outfile).json \
        -c $(cachefile).json \
    ```
    Noted:

    + `$(link)` could be one or multiple. If multiple links, spearated them by white space.
    + `$(outfile)` and `$(cachefile)` could be same or different. Both of them must be json file.
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

---

## Be Careful

Because of request limits that are common settings on public website, they may lock your IP address if you request too frequently. Therefore, set the time limit in your code, just like `time.sleep(20)`.

Also, you should use WIFI from your phone to do web crawler. Once your IP address is locked, you can turn on flight mode and then turn off, and re-open your WIFI to change your IP address. (p.s., WIFI ip address is floating.)
