#!/bin/bash
export PYTHONPATH=./

## Check if OUTPUT_DIR exists
OUTPUT_DIR=out/googlenews
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "$OUTPUT_DIR does not exist, so create it."
    mkdir $OUTPUT_DIR
fi

## Variables
TODAY=$(date +"%Y%m%d")
INPUT_QUERY_FILE=src/gnews_query.txt
OUTPUT_FILE=${OUTPUT_DIR}/googlenews_${TODAY}.json

if [ ! -f "$OUTPUT_FILE" ]; then

    echo "Hello! This is a brand new day."
    python src/entry_gnews.py \
        -iq $INPUT_QUERY_FILE \
        -o $OUTPUT_FILE

else

    echo "There is a cache file in local."
    CACHE_FILE=$OUTPUT_FILE

    python src/entry_gnews.py \
        -iq $INPUT_QUERY_FILE \
        -o $OUTPUT_FILE \
        -c $CACHE_FILE
fi
