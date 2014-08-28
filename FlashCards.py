#!/bin/bash

# Author: Chris Robertson <electronicsleep@gmail.com>
# Date: 08/27/2014
# Purpose: Simple FlashCard app for learning python
# Released under the MIT license

# Running:
# python FlashCards.py User

from random import randint
from sys import argv

script, user_name = argv
prompt = '> '
cardFront=""

### CARD FUNCTIONS ###

def showQuestionCard(cardFront):
 
        print "----------"
        print "|         |"
        print "|  %s    " % cardFront
        print "|         |"
        print "----------"
 
def showAnswerCard(cardBack):
 
        print "----------"
        print "|         |"
        print "|  %s    " % cardBack
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

#DEFINE SINGLE CARD
card = {}

#FIND HOW MANY CARDS
n = len(cards.keys())
print "NUMBER OF CARDS %s" % n

randomNum = randint(1,n)

# Loop over items and unpack each item.
i = 0
for k, v in cards.items():

    i += 1
    if (i == randomNum):
        cardFront = k
        cardBack = v


showQuestionCard(cardFront)

#ASK FOR ANSWER

print "Hi %s, %s " % (user_name, script)
print "What is the answer? "
answer = raw_input(prompt)

#EVAULATE ANSWER

if (answer == cardBack):
 print "*** CORRECT ***"
else:
 print "*** INCORRECT ***"
 print "the answer is: "
 print cardBack

showAnswerCard(cardBack)
