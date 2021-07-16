# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Example code

import argparse
import logging
import os
import sys

from src.goodinfo import get_all_basic, get_code_name, readJson, writeJson

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def parse_args():

    parser = argparse.ArgumentParser(description="Web Crawler for Good Info.")
    parser.add_argument(
        "-g1",
        "--get_code_and_name_only",
        action="store_true",
        help="only get stock codes and abbrev. names of companies in Taiwan",
    )
    parser.add_argument(
        "-g2",
        "--get_all_basic",
        action="store_true",
        help="get basic information of companies in Taiwan",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default="out/company.json",
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
    logger.info(args)

    if not args.get_code_and_name_only and not args.get_all_basic:
        raise ValueError(
            "What do you want this program do ?"
            "Please use `python main.py --help` to check the arguments."
        )

    if (
        (not args.get_code_and_name_only)
        and (args.get_all_basic)
        and (not args.cache_file)
    ):
        logger.warning(
            "We do not only support g2=True without g1=True and cache_file, "
            f"so we turn g1 is True. and save json file to {args.output_file}."
        )
        args.get_code_and_name_only = True

    # make directory if it does not exist
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    """ Get Code & Name """
    if args.get_code_and_name_only:
        logger.info("=== Get code & name from URL ===")
        data = get_code_name()

        # ensure if user want to cover local file that exists.
        if os.path.isfile(args.output_file):
            proceed = input(f"{args.output_file} file exists, wanna cover it ? (y/n): ")
            if proceed == "n":
                sys.exit()

        writeJson(data, args.output_file)

    """ Get Basic Info """
    if args.get_all_basic:
        logger.info("=== Get basic info from URL ===")
        data = readJson(args.cache_file if args.cache_file else args.output_file)
        get_all_basic(data, args.output_file)


if __name__ == "__main__":
    main()
