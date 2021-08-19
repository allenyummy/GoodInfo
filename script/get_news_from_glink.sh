#!/bin/bash
export PYTHONPATH=./

## Variables
TODAY=$(date +"%Y%m%d")
INPUT_FILE=out/googlenews/googlenews_${TODAY}.json

function _resolve_media_zh2en() {
    python - ${1} <<END
import sys
from src.config import MEDIA_NAME
print (MEDIA_NAME[sys.argv[1]])
END
}

TOTAL_SIZE=$(cat $INPUT_FILE | jq 'length|tonumber')
i=0

for row in $(cat $INPUT_FILE | jq -r '.[] | @base64'); do

    _resolve() {
        echo ${row} | base64 --decode | jq -r ${1}
    }

    ## Get MEDIA and LINK
    MEDIA=$(_resolve '.media')
    LINK=$(_resolve '.link')
    MEDIA_EN=$(_resolve_media_zh2en ${MEDIA})

    ## Check if OUTPUT_DIR exists
    OUTPUT_DIR=out/media/${MEDIA_EN}
    if [ ! -d "$OUTPUT_DIR" ]; then
        echo "$OUTPUT_DIR does not exist, so create it."
        mkdir $OUTPUT_DIR
    fi

    # Check if OUTPUT_FILE exists
    OUTPUT_FILE=${OUTPUT_DIR}/${MEDIA_EN}_${TODAY}.json
    if [ ! -f "$OUTPUT_FILE" ]; then

        # echo "Hello! This is a brand new day for ${MEDIA} ${MEDIA_EN}."
        python src/entry_media.py \
            -m $MEDIA_EN \
            -l $LINK \
            -o $OUTPUT_FILE

    else

        # echo "There is a cache file for ${MEDIA} ${MEDIA_EN} in local."
        CACHE_FILE=$OUTPUT_FILE

        python src/entry_media.py \
            -m $MEDIA_EN \
            -l $LINK \
            -o $OUTPUT_FILE \
            -c $CACHE_FILE
    fi

    ## Progress
    i=$(($i + 1))
    echo -ne "Progress $i/$TOTAL_SIZE: $(($(($i * 100 / $TOTAL_SIZE))))%\r"

done
