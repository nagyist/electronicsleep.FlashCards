#!/bin/bash

# Author: Chris Robertson https://github.com/electronicsleep
# Date: 05/02/2016
# Purpose: Simple FlashCard app for learning math and python
# Released under the BSD license

# Running:
# bash FlashCards.py

END_CARD=$(echo $RANDOM % 100 + 1 | bc)
DECK=$(cat memorize.txt)
IFS=$'\n'

echo "SHUFFLE"

NUM=0
for CARD in $DECK; do

 if [[ "$CARD" == *"Q."* ]]; then
  QCARD="$CARD"
 elif [[ "$CARD" == *"A."* ]]; then
  ACARD="$CARD"
  NUM=$((NUM+1))
  if [ "$NUM" -eq "$END_CARD" ]; then
   break
  fi 
 fi

done

echo "$QCARD" && sleep 2 && echo "$ACARD"

exit 0
