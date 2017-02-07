#!/usr/bin/python

# Author: Chris Robertson <electronicsleep@gmail.com>
# Date: 09/10/2014
# Purpose: Simple FlashCard app for learning math and python
# Released under the BSD license
# Works with python 2 and 3

# Running:
# python FlashCards.py

# IMPORT STANDARD FUNCTIONS ###

import time
import datetime
import sys
# import traceback

from random import randint
from sys import argv

# PRINT NUMBER OF ARGUMENTS
# print(len(sys.argv))

if len(sys.argv) == 1:
    script = argv
    user_name = "Emtpy"
elif len(sys.argv) == 2:
    script, user_name = argv

timeStart = time.time()

prompt = '> '
cardFront = ""

# CARD FUNCTIONS


def showQuestionCard(cardFront):
    print("\---------------------------/")
    print("|///////////////////////////|")
    print("|///////////////////////////|")
    print("| Q. %s                " % cardFront.strip())
    print("|///////////////////////////|")
    print("|///////////////////////////|")
    print("\---------------------------/")


def showAnswerCard(cardBack):
    print("\---------------------------/")
    print("|                           |")
    print("|                           |")
    print("| A. %s               " % cardBack.strip())
    print("|                           |")
    print("|                           |")
    print("\---------======------------/")


# SETUP CARD DICTIONARY

# INITIAL SETUP
cards = {}

# HARDCODED EXAMPLE CARDS
# cards['3 * 2'] = '6'
# cards['4 * 11'] = '44'
# cards['8 * 2'] = '16'
# cards['11 - 100'] = '89'
# cards['110 - 100'] = '-10'
# cards['5 + 5'] = '10'


# IMPORT MORE CARDS FROM FILE

try:
    file = open('memorize.txt', 'r')
except:
    print("Please create a memorize.txt file")
    exit()


# PRINT ENTIRE FILE OF QA CARDS
# print file.read()

# PARSE FILE FOR QUESTION AND ANSWER FOR CARDS

for line in file:
    if line.startswith('Q'):
        first, _, questionline = line.partition(" ")
        #print("Question: " + line,)
    elif line.startswith('A'):
        first, _, answerline = line.partition(" ")
        cards[questionline] = answerline
        #print("Answer: " + line,)

file.close()

# DEFINE SINGLE CARD
card = {}

# FIND HOW MANY CARDS

n = len(cards.keys())
print("\=====-----======--------=====/")
print("NUMBER OF CARDS %s" % n)
print("DATE: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))


num_cards = 4

num_correct = 0
num_incorrect = 0

for i in range(num_cards):

    randomNum = randint(1,n)

    # LOOP AND UNPACK ONE RANDOM CARD
    i = 0
    for k, v in cards.items():

        i += 1
        if (i == randomNum):
            cardFront = k
            cardBack = v


    showQuestionCard(cardFront)

    print("What is the answer? ")

    try:
        input = raw_input
    except:
        pass

    answer = input(prompt)

    # EVAULATE ANSWER
    answer = answer.lower()
    answerCard = cardBack.lower()

    if answer.strip() == answerCard.strip():
         print("*** CORRECT ***")
         num_correct += 1
         print "Num Correct: " + str(num_correct)
    else:
         print("*** INCORRECT ***")
         print("The correct answer is:")
         print("the answer is: |")
         print(cardBack.strip())
         print("|")
         num_incorrect += 1
         print "Num Incorrect: " + str(num_incorrect)

    showAnswerCard(cardBack)

    # GET END TIME
    timeEnd = time.time()

    # PRINT TIME IT TAKES TO ANSWER
    diff = timeEnd - timeStart
    diff_str = str(diff)
    print("DATE: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    print("You took " + diff_str + " seconds to answer")
    percent_correct = ((float(num_correct) / float(num_cards)) * 100)
    print str(percent_correct) + "% Correct"


# END OF SCRIPT
sys.exit(0)
