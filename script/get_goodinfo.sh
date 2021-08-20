#!/bin/bash
export PYTHONPATH=./

## Check if OUTPUT_DIR exists
OUTPUT_DIR=out/goodinfo
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "$OUTPUT_DIR does not exist, so create it."
    mkdir $OUTPUT_DIR
fi

## Variables
OUTPUT_FILE=${OUTPUT_DIR}/company.json

if [ ! -f "$OUTPUT_FILE" ]; then

    echo "Hello! This is a brand new day."
    python src/entry_goodinfo.py \
        -o $OUTPUT_FILE

else

    echo "There is a cache file in local."
    CACHE_FILE=$OUTPUT_FILE

    python src/entry_goodinfo.py \
        -o $OUTPUT_FILE \
        -c $CACHE_FILE
fi
