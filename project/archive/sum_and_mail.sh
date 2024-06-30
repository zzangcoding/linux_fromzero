#!/bin/bash

WATCH_DIR="."

inotifywait -m -e close_write --format "%w%f" "$WATCH_DIR" | while read -r FILE;do
	if [[ "$FILE" == *.mp4 ]];then
		echo "New vieo file deteced: $FILE"

		../whisper "$FILE" --output_format txt --output_dir ./transcriptions
		TRANSCRIPTION_FILE="./transcriptions/$(basename "$FILE" .mp4).txt"

		cp $TRANSCRIPTION_FILE ./transcriptions/tmp.txt

		python3 ./sum_gpt.py 

		mutt -s "LIVE SUMMARY!" jonhpark@naver.com < ./transcriptions/summary.txt
	fi
done

