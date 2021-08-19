# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Example code

import argparse
import logging
import os
import sys
import time
from tqdm import tqdm

from src.utils.struct import GoodInfoStruct
from src.utils.utility import readJson, writeJson
from src.crawler.goodinfo.goodinfo import get_code_name, get_basic

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger(__name__)


def parse_args():

    parser = argparse.ArgumentParser(description="Web Crawler for Good Info.")
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        help="output file to store the results",
    )
    parser.add_argument(
        "-c",
        "--cache_file",
        type=str,
        help="read cache file to accelerate the program",
    )
    args = parser.parse_args()
    return args


def main():

    """Args"""
    args = parse_args()
    logger.info(f"ARGS: {args}\n")

    """ Get basic from cache """
    cache = None
    if args.cache_file:
        cache = readJson(infile=args.cache_file)
        cache = [GoodInfoStruct(**c) for c in cache]
    else:
        cache = get_code_name()

    """ Get basic from goodinfo website """
    data = list()
    for i, c in enumerate(
        tqdm(
            cache,
            total=(len(cache)),
            desc="Get Basic Info",
        )
    ):

        try:

            if c.公司名稱:
                goodinfo = c
            else:
                goodinfo = get_basic(c.股票代號)

        except Exception as e:

            logger.error(f"{c.股票代號}, {e}")

            """ Write data """
            if args.output_file:
                os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
                writeJson(
                    data=[d.__2dict__() for d in data]
                    + [c.__2dict__() for c in cache[i:]],
                    outfile=args.output_file,
                )
            sys.exit()

        else:

            data.append(goodinfo)

            if i > 0 and i % 10 == 0:
                logger.info(f"write file to {i}")

                """ Write data """
                if args.output_file:
                    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
                    writeJson(
                        data=[d.__2dict__() for d in data]
                        + [c.__2dict__() for c in cache[i + 1 :]],
                        outfile=args.output_file,
                    )

                time.sleep(15)


if __name__ == "__main__":
    main()
