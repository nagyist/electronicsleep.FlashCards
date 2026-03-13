FlashCards
==========

Open Source Flash Card Application for learning and Memorizing anything

Author: Chris Robertson

License: Released under the BSD license

Purpose: A simple Open Source Flash Card App for kids or really anyone to memorize programming and math.
I got the idea for this program to keep my mind sharp and wanted to remember facts I have to look 
up often with a goal of being a better programmer and human. I left the application as simple as 
possible so that anyone can extend the functionality without much complexity. 

Update the information you want to memorize into the memorize.txt file and run.

# Python Usage:
```
Open Terminal
git clone https://github.com/electronicsleep/flash-cards.git
cd flash-cards
python3 create-cards.py
python3 flash-cards.py
```

Memorize test file format: (memorize.txt)
```
Q. Questions
A. Answers
```

![Screenshot CLI](screenshot-cli.jpg?raw=true "ScreenShot CLI")


Todo/Ideas:
* Remember last 3 cards to prevent duplicates
* Make cards for all different things
* Use as a todo application or terms list
* GUI interface for the cards using wxwidgets
* Loop in the main program with quit
* Stats on answered questions, time, topscore
* Save stats file save and load for future use
* Compete with others locally or on the net
* Website to post top scores via an API call
* iPhone version, Android version
* More math game ideas

Resources:
https://www.python.org/
