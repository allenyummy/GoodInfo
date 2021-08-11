# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Utility function

import json


def readJson(infile: str):
    with open(infile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    return data


def writeJson(data: json, outfile: str):

    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
