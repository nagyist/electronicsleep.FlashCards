#!/usr/bin/python

# Author: Chris Robertson https://github.com/electronicsleep
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


def show_question_card(card_front):
    print("\---------------------------/")
    print("|///////////////////////////|")
    print("|///////////////////////////|")
    print("| Q. %s                " % card_front.strip())
    print("|///////////////////////////|")
    print("|///////////////////////////|")
    print("\---------------------------/")


def show_answer_card(cardBack):
    print("\---------------------------/")
    print("|                           |")
    print("|                           |")
    print("| A. %s               " % cardBack.strip())
    print("|                           |")
    print("|                           |")
    print("\---------======------------/")


def main():

    # PRINT NUMBER OF ARGUMENTS
    # print(len(sys.argv))

    if len(sys.argv) == 1:
        script = argv
        user_name = "Emtpy"
    elif len(sys.argv) == 2:
        script, user_name = argv

    time_start = time.time()

    prompt = '> '
    card_front = ""

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
        mem_file = open('memorize.txt', 'r')
    except:
        print("Please create a memorize.txt file")
        exit()

    # PRINT ENTIRE FILE OF QA CARDS
    # print mem_file.read()

    # PARSE FILE FOR QUESTION AND ANSWER FOR CARDS

    for line in mem_file:
        if line.startswith('Q'):
            first, _, question_line = line.partition(" ")
            # print("LOAD: Question: " + line,)
        elif line.startswith('A'):
            first, _, answer_line = line.partition(" ")
            cards[question_line] = answer_line
            # print("LOAD: Answer: " + line,)

    mem_file.close()

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

    for x in range(num_cards):

        randomNum = randint(1,n)

        # LOOP AND UNPACK ONE RANDOM CARD
        i = 0
        for k, v in cards.items():

            i += 1
            if i == randomNum:
                card_front = k
                card_back = v

        show_question_card(card_front)

        print("What is the answer? ")

        try:
            input = raw_input
        except:
            pass

        answer = input(prompt)

        # EVALUATE ANSWER
        answer = answer.lower()
        answer_card = card_back.lower()

        if answer.strip() == answer_card.strip():
            print("*** CORRECT ***")
            num_correct += 1
            print "Num Correct: " + str(num_correct)
        else:
            print("*** INCORRECT ***")
            print("The correct answer is:")
            print("the answer is: |")
            print(card_back.strip())
            print("|")
            num_incorrect += 1
            print "Num Incorrect: " + str(num_incorrect)

        show_answer_card(card_back)

        # GET END TIME
        time_end = time.time()

        # PRINT TIME IT TAKES TO ANSWER
        diff = time_end - time_start
        diff_str = str(diff)
        print("DATE: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print("You took " + diff_str + " seconds to answer")
        percent_correct = ((float(num_correct) / float(num_cards)) * 100)
        if percent_correct > 75:
            print ("Good Job!")
        print str(percent_correct) + "% Correct"

if __name__ == "__main__":
    main()
