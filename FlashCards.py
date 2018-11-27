#!/usr/bin/python

# Author: Chris Robertson https://github.com/electronicsleep
# Purpose: Simple FlashCard app for learning math and python
# Released under the BSD license

# Running:
# python FlashCards.py

import time
import datetime
import sys

from random import randint
from sys import argv


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

    cards = {}
    mem_file = ""
    question_line = ""

    # Import cards from file
    try:
        mem_file = open('memorize.txt', 'r')
    except Exception as e:
        print("Please create a memorize.txt file")
        print("Error: " + str(e))
        exit()

    for line in mem_file:
        if line.startswith('Q.'):
            first, _, question_line = line.partition(" ")
            print("LOAD: Question: " + line)
        elif line.startswith('A.'):
            first, _, answer_line = line.partition(" ")
            cards[question_line] = answer_line
            print("LOAD: Answer: " + line)

    mem_file.close()

    n = len(cards.keys())
    print("\=====-----======--------=====/")
    print("NUMBER OF CARDS %s" % n)
    print("DATE: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    num_cards = 4

    num_correct = 0
    num_incorrect = 0

    for x in range(num_cards):

        random_num = randint(1, n)

        # Loop and deal one random card
        i = 0
        for k, v in cards.items():

            i += 1
            if i == random_num:
                card_front = k
                card_back = v

        show_question_card(card_front)

        print("What is the answer? ")

        answer_str = raw_input(prompt)
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

        time_end = time.time()

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
