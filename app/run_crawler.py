# encoding=utf-8
# Author: Yu-Lun Chiang
# Description:

import logging
import os
from tqdm import tqdm
from src.utils.utility import readJson, writeJson
from src.config import MEDIA_NAME
from src.crawler.media_news_crawler_factory import MediaNewsCrawlerFactory
from src.utils.struct import NewsStruct

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger(__name__)


def main():

    infile = "out/googlenews_wo_company.json"
    outdir = "out/"

    data = readJson(infile)

    for d in tqdm(
        data,
        total=(len(data)),
        desc="Get Google News of Company",
    ):

        logger.info("==== CRAWLING ====")
        link = d["link"]
        logger.info(f"link: {link}")

        """ MAKE DIR """
        media_en_name = MEDIA_NAME[d["media"]]
        outfile_dir = os.path.join(outdir, media_en_name)
        outfile_path = os.path.join(outfile_dir, f"{media_en_name}.json")
        os.makedirs(outfile_dir, exist_ok=True)

        """ READ CACHE """
        cache = None
        if os.path.exists(outfile_path):
            cache = readJson(outfile_path)
            cache = [NewsStruct(**c) for c in cache]

        """ JUST PASS IF ALREADY EXISTS """
        if cache and any(link == c.link for c in cache):
            logger.info("This Link exists in cache file.")
            logger.info("PASS\n\n")
            continue

        """ INIT NEWSCRAWLER """
        nc = MediaNewsCrawlerFactory(media_en_name)

        """ CRAWLER """
        try:
            news = nc.getInfo(link=link)
        except Exception as e:
            logger.error(f"Error message: {e}\n")
        else:
            logger.info("got news !!")
            data = cache + [news] if cache else [news]
            writeJson(
                data=[d.__2dict__() for d in data],
                outfile=outfile_path,
            )
            logger.info("==== FINISHED ====\n\n")


if __name__ == "__main__":
    main()
