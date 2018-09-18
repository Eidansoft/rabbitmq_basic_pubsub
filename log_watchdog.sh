#!/bin/bash
# Simple script to look for a pattern into a log trace and trigger a command when it found it.

PATERN="$1"
COMMAND="$2"

while read line ; do
    echo "$line"
    echo "$line" | grep -q $PATERN
    if [ $? = 0 ]
    then
         eval $COMMAND
    fi
done <&0
