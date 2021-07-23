# Web Crawler for Taiwan GoodInfo

It's a web crawler to get information of listed companies, including their english names, chinese names, abbreviation, codes, and important related people. Besides, it also gets news of these companies. The goal is to build up a dataset for financial news to help the development of Chinese Natural Language Processing.

---

## Prepare Environment (if you want to get info by yourself)

+ Run below commands to ensure virtual `conda` environment that has `poetry`.
```
$ conda create --name GoodInfo-py38 python=3.8
$ conda activate GoodInfo-py38
$ pip install poetry
```

+ Install packages into virtual conda environment
```
$ git clone https://github.com/allenyummy/GoodInfo.git
$ poetry install
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

---

## Be Careful

Because of request limits that are common settings on public website, they may lock your IP address if you request too frequently. Therefore, set the time limit in your code, just like `time.sleep(20)`.

Also, you should use WIFI from your phone to do web crawler. Once your IP address is locked, you can turn on flight mode and then turn off, and re-open your WIFI to change your IP address. (p.s., WIFI ip address is floating.)
