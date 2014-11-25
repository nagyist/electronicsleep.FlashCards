#!/usr/bin/python

# Author: Chris Robertson <electronicsleep@gmail.com>
# Date: 09/10/2014
# Purpose: Simple FlashCard app for learning math and python
# Released under the MIT license

# Running:
# python FlashCards.py Hello! 

### IMPORT STANDARD FUNCTIONS ###

import time
import datetime
import sys
import traceback

from random import randint
from sys import argv

if len(sys.argv)==1:
    print 'Usage: python FlashCards.py Name'
    sys.exit(0)


timeStart = time.time()

script, user_name = argv
prompt = '> '
cardFront=""

### CARD FUNCTIONS ###

def showQuestionCard(cardFront):
 
        print "----------"
        print "|////////|"
        print "| %s    " % cardFront.strip()
        print "|////////|"
        print "----------"
 
def showAnswerCard(cardBack):
 
        print "----------"
        print "|         |"
        print "| %s    " % cardBack.strip()
        print "|         |"
        print "----------"


### SETUP CARD DICTIONARY ###

#INITIAL SETUP
cards = {'2+2': '4', '3+3': '6'}

#ADD SOME MORE CARDS
cards['3 * 2'] = '6'
cards['4 * 11'] = '44'
cards['8 * 2'] = '16'
cards['24 / 6'] = '4'
cards['100 / 10'] = '10'
cards['REDUCE: 2/10'] = '1/5'
cards['REDUCE: 10/100'] = '1/10'
cards['11 - 100'] = '89'
cards['110 - 100'] = '-10'
cards['5 + 5'] = '10'


#IMPORT MORE CARDS FROM FILE
file = open('memorize.txt', 'r')

#PRINT ENTIRE FILE OF QA CARDS
#print file.read()

#PARSE FILE FOR QUESTION AND ANSWER FOR CARDS
for line in file:
    if line.startswith('Q'):
        first, _, questionline = line.partition(" ")
        #print "Question: " + line,
    elif line.startswith('A'):
        first, _, answerline = line.partition(" ")
        cards[questionline] = answerline
        #print "Answer: " + line,

file.close()

#DEFINE SINGLE CARD
card = {}

#FIND HOW MANY CARDS
n = len(cards.keys())
print "NUMBER OF CARDS %s" % n

randomNum = randint(1,n)

#LOOP AND UNPACK ONE RANDOM CARD
i = 0
for k, v in cards.items():

    i += 1
    if (i == randomNum):
        cardFront = k
        cardBack = v


showQuestionCard(cardFront)

#ASK FOR ANSWER

print "Date: " ,datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
print "Hi %s, %s " % (user_name, script)
print "What is the answer? "
answer = raw_input(prompt)

#EVAULATE ANSWER

answer=answer.lower()
answerCard=cardBack.lower()

if answer.strip() == answerCard.strip():
 print "*** CORRECT ***"
else:
 print "*** INCORRECT ***"
 print "the answer is: |"
 print cardBack.strip()
 print "|"

showAnswerCard(cardBack)

#GET END TIME

timeEnd = time.time()

#PRINT TIME IT TAKES TO ANSWER

diff = timeEnd - timeStart
diff_str = str(diff)
print "You took " + diff_str + " seconds to answer"

#END OF SCRIPT

sys.exit(0)
