#!/usr/bin/python

# Author: Chris Robertson https://github.com/electronicsleep
# Date: 09/10/2014
# Purpose: Simple FlashCard app for learning math and python
# Released under the BSD license
# Works with python 2 and 3

# Running:
# python FlashCards.py

# IMPORT LIBRARIES

import time
import datetime
import sys

from random import randint
from sys import argv

# CARD FUNCTIONS


def show_question_card(card_front):
    print("\---------------------------/")
    print("|///////////////////////////|")
    print("|                           |")
    print("| Q. %s                " % card_front.strip())
    print("|                           |")
    print("|///////////////////////////|")
    print("\---------------------------/")


def show_answer_card(card_back):
    print("\---------------------------/")
    print("|                           |")
    print("|                           |")
    print("| A. %s               " % card_back.strip())
    print("|                           |")
    print("|                           |")
    print("\---------======------------/")


def main():

    # PRINT NUMBER OF ARGUMENTS
    # print(len(sys.argv))

    if len(sys.argv) == 2:
        script, username = argv
    else:
        script = argv
        username = "Emtpy"

    print("Script:", script)
    print("User: ", username)

    time_start = time.time()

    prompt = '> '
    card_front = ""

    # SETUP CARD DICTIONARY

    # INITIAL SETUP
    cards = {}
    mem_file = ""
    question_line = ""

    # IMPORT MORE CARDS FROM FILE
    try:
        mem_file = open('memorize.txt', 'r')
    except Exception as e:
        print("Please create a memorize.txt file")
        print("Error: " + str(e))
        exit()

    # PRINT ENTIRE FILE OF QA CARDS
    # print mem_file.read()

    # PARSE FILE FOR QUESTION AND ANSWER FOR CARDS

    for line in mem_file:
        if line.startswith('Q.'):
            first, _, question_line = line.partition(" ")
            # print("LOAD: Question: " + line,)
        elif line.startswith('A.'):
            first, _, answer_line = line.partition(" ")
            cards[question_line] = answer_line
            # print("LOAD: Answer: " + line,)

    mem_file.close()

    # FIND HOW MANY CARDS

    n = len(cards.keys())
    print("\=====-----======--------=====/")
    print("NUMBER OF CARDS %s" % n)
    print("DATE: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    num_cards = 4

    num_correct = 0
    num_incorrect = 0

    for x in range(num_cards):

        random_num = randint(1, n)

        # LOOP AND UNPACK ONE RANDOM CARD
        i = 0
        for k, v in cards.items():

            i += 1
            if i == random_num:
                card_front = k
                card_back = v

        show_question_card(card_front)

        print("What is the answer? ")

        answer = input(prompt)
        answer_str = str(answer)
        answer_str = answer_str.lower()
        answer_card = card_back.lower()

        if answer_str.strip() == answer_card.strip():
            print("*** CORRECT ***")
            num_correct += 1
            print("Num Correct: ", num_correct)
        else:
            print("*** INCORRECT ***")
            print("The correct answer is:")
            print("the answer is: |")
            print(card_back.strip())
            print("|")
            num_incorrect += 1
            print("Num Incorrect: ", num_incorrect)

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
        print(percent_correct, "% Correct")


if __name__ == "__main__":
    main()
