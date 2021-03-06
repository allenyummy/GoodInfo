# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Entry program to get news from media

import argparse
import logging
import os

from src.crawler.media.factory import MediaNewsCrawlerFactory
from src.utils.struct import NewsStruct
from src.utils.utility import readJson, writeJson

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger(__name__)


def parse_args():

    parser = argparse.ArgumentParser(
        description="Web Crawler for News fomr Media.",
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


def main():

    """Args"""
    args = parse_args()
    logger.debug(f"ARGS: {args}\n")

    """ Get news from cache """
    cache = None
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

        """ JUST PASS IF ALREADY EXISTS """
        if cache and any(link == c.link for c in cache):
            logger.info("This Link exists in cache file.")
            logger.info("PASS\n\n")
            continue

        try:
            news = nc.getInfo(link=link)

        except Exception as e:
            logger.error(f"{link} -> Error message: {e}\n")

        else:
            logger.info("got news !!")
            news_list.append(news)

        logger.info("==== FINISHED ====\n\n")

    """ Merge cache and latest news """
    data = cache + news_list if cache else news_list

    """ Write data """
    if args.output_file:
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
        writeJson(
            data=[d.__2dict__() for d in data],
            outfile=args.output_file,
        )


if __name__ == "__main__":
    main()
