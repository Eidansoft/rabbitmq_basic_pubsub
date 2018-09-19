#!/bin/bash
# Simple script to look for a pattern into a log trace and trigger a command when it found it.

PATTERN="$1"
COMMAND="$2"

[ -z "$PATTERN" -o -z "$COMMAND" ] && echo "[ERROR] The pattern and the command are mandatory params" && exit 1

while read line ; do
    echo "$line"
    echo "$line" | grep -q $PATTERN
    if [ $? = 0 ]
    then
         eval $COMMAND
    fi
done <&0
