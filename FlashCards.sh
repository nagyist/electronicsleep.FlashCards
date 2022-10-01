#!/bin/bash

# Author: Chris Robertson https://github.com/electronicsleep
# Date: 05/02/2016
# Purpose: Simple FlashCard app for learning math and python
# Released under the BSD license

# Running:
# bash FlashCards.sh

DECK=$(cat memorize.txt)
IFS=$'\n'

echo "Shuffle"
DRAW_CARD=$(( $RANDOM % 10 + 1 ))
echo "Draw Card: $DRAW_CARD"

NUM=0
for CARD in $DECK; do

  if [[ "$CARD" == *"Q."* ]]; then
    QCARD="$CARD"
  elif [[ "$CARD" == *"A."* ]]; then
    ACARD="$CARD"
    NUM=$((NUM+1))
    if [ "$NUM" -eq "$DRAW_CARD" ]; then
      break
    fi
 fi

done

  echo "$QCARD" && sleep 2 && echo "$ACARD"

exit 0
