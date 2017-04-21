#!/bin/bash

# Author: Chris Robertson https://github.com/electronicsleep
# Date: 12/03/2016
# Purpose: Combine Memorize Files for FlashCards
# Released under the BSD license

# Running:
# bash combine.sh

cp memorize.txt memorize_backup.txt

FILES=$(ls *memorize*)

echo -e "#COMBINE MEMORIZE FILES\n" > memorize.txt

for FILE in $FILES
do

 if [ "$FILE" == 'memorize.txt' ];then
  continue
 fi

 if [ "$FILE" == 'memorize_backup.txt' ];then
  continue
 fi

 echo "$FILE"

 echo -e "\n#FILE: $FILE\n" >> memorize.txt

 cat "$FILE" >> memorize.txt

done

exit 0
