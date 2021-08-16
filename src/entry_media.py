# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import argparse
import logging
import os

from src.crawler.media import (
    appledaily,
    bcc,
    bnext,
    chinatimes,
    cmmedia,
    cna,
    ctee,
    cts,
    cynes,
    digitimes,
    ebc,
    ettoday,
    ftv,
    ltn,
    mirror,
    moneydj,
    moneyudn,
    sina,
    storm,
    technews,
    ttv,
    udn,
    wealth,
    yahoo,
)
from src.utils.struct import NewsStruct
from src.utils.utility import readJson, writeJson

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger(__name__)


def parse_args():

    parser = argparse.ArgumentParser(
        description="Web Crawler for News.",
    )
    parser.add_argument(
        "-m",
        "--media",
        type=str,
        help="Determine the class of media crawler that needs to be instantiated.",
    )
    parser.add_argument(
        "-l",
        "--link",
        type=str,
        nargs="+",
        help="Target news link.",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        help="store data into output file.",
    )
    parser.add_argument(
        "-c",
        "--cache_file",
        type=str,
        help="get data from a cache file.",
    )
    args = parser.parse_args()
    return args


def MediaNewsCrawlerFactory(media_name: str):

    LOCALIZERS = {
        "appledaily": appledaily.AppleDailyNewsCrawler,
        "bcc": bcc.BCCNewsCrawler,
        "bnext": bnext.BnextNewsCrawler,
        "chinatimes": chinatimes.ChinatimesNewsCrawler,
        "cmmedia": cmmedia.CMMediaNewsCrawler,
        "cna": cna.CNANewsCrawler,
        "ctee": ctee.CTEENewsCrawler,
        "cts": cts.CTSNewsCrawler,
        "cynes": cynes.CYNESNewsCrawler,
        "digitimes": digitimes.DigitimesNewsCrawler,
        "ebc": ebc.EBCNewsCrawler,
        "ettoday": ettoday.ETtodayNewsCrawler,
        "ftv": ftv.FTVNewsCrawler,
        "ltn": ltn.LTNNewsCrawler,
        "mirror": mirror.MirrorNewsCrawler,
        "moneydj": moneydj.MoneyDJNewsCrawler,
        "moneyudn": moneyudn.MoneyUDNNewsCrawler,
        "sina": sina.SINANewsCrawler,
        "storm": storm.StormNewsCrawler,
        "technews": technews.TechnewsNewsCrawler,
        "ttv": ttv.TTVNewsCrawler,
        "udn": udn.UDNNewsCrawler,
        "wealth": wealth.WealthNewsCrawler,
        "yahoo": yahoo.YahooNewsCrawler,
    }
    return LOCALIZERS[media_name]()


def main():

    """Args"""
    args = parse_args()
    logger.info(f"ARGS: {args}\n")

    """ Get news from cache """
    if args.cache_file:
        cache = readJson(infile=args.cache_file)
        cache = [NewsStruct(**c) for c in cache]

    """ Instantiate NewsCrawler """
    nc = MediaNewsCrawlerFactory(args.media)

    """ Get news from link """
    news_list = list()
    for link in args.link:
        logger.info("==== CRAWLING ====")
        logger.info(f"link: {link}")
        try:
            news = nc.getInfo(link=link)
        except Exception as e:
            logger.error(f"Error message: {e}\n")
        else:
            logger.info("got news !!")
            news_list.append(news)
        logger.info("==== FINISH ====\n\n")

    """ Merge cache and latest news """
    data = cache + news_list if args.cache_file else news_list

    """ Write data """
    if args.output_file:
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
        writeJson(
            data=[d.__2dict__() for d in data],
            outfile=args.output_file,
        )


if __name__ == "__main__":
    main()
