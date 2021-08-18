# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Entry program to get news from google

import argparse
import logging
from tqdm import tqdm
import random
import time
import os

from src.utils.struct import GoogleNewsStruct
from src.utils.utility import readJson, writeJson
from src.crawler.googlenews import gnews

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger(__name__)


def parse_args():

    parser = argparse.ArgumentParser(
        description="Web Crawler for Google News.",
    )
    parser.add_argument(
        "-iq",
        "--input_query_file",
        type=str,
        help="input query file (one query per line).",
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


def write(args, cache, news_list):

    """Merge cache and latest news"""
    data = cache + news_list if args.cache_file else news_list

    """ Write data """
    if args.output_file:
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
        writeJson(
            data=[d.__2dict__() for d in data],
            outfile=args.output_file,
        )


def sleep():
    sleeptime = random.uniform(30, 50)
    logger.info(f"sleep for: {sleeptime} seconds.")
    time.sleep(sleeptime)


def main():

    """Args"""
    args = parse_args()
    logger.info(f"ARGS: {args}\n")

    """ Get news from cache """
    cache = None
    if args.cache_file:
        cache = readJson(infile=args.cache_file)
        cache = [GoogleNewsStruct(**c) for c in cache]

    """ Get query from input query file """
    query_list = list()
    with open(
        args.input_query_file,
        "r",
        encoding="utf-8",
    ) as f:
        for line in f:
            query_list.append(line.strip())
        f.close()

    random.shuffle(query_list)

    """ Instantiate GoogleNewsCrawler """
    gnc = gnews.GoogleNewsCrawler()

    """ Get news from google """
    news_list = list()
    write_every_n_companies = random.randint(20, 39)

    for i, query in enumerate(
        tqdm(
            query_list,
            total=(len(query_list)),
            desc="Get Google News of Company",
        )
    ):

        logger.info("==== CRAWLING ====")
        logger.info(f"query: {query}")

        try:
            news = gnc.getInfo(query=query)

        except Exception as e:

            logger.error(f"Error message: {e}")
            logger.info(f"write all to {i}\n\n")
            write(args, cache, news_list)

        else:

            logger.info(f"got news {len(news)}!!")
            for n in news:
                if cache:
                    if n not in cache and n not in news_list:
                        news_list.append(n)
                else:
                    if n not in news_list:
                        news_list.append(n)
            logger.info("==== FINISHED ====\n\n")

        if i > 0 and i % write_every_n_companies == 0:
            logger.info(f"write file to {i}")
            write(args, cache, news_list)
            sleep()
            write_every_n_companies = random.randint(20, 39)
            logger.info(f"reset write_every_{write_every_n_companies}_companies.")

    logger.info(f"write all to {i}")
    write(args, cache, news_list)


if __name__ == "__main__":
    main()
