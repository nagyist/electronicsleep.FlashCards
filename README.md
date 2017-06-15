FlashCards
==========

Open Source Flash Card Application for learning Python and Memorizing anything

Author: Chris Robertson

License: Released under the BSD license

Purpose: A simple Open Source Flash Card Application for anyone to memorize programming and math. 
I got the idea for this program to keep my mind sharp and wanted to remember facts I have to look 
up often with a goal of being a better programmer and human. I left the application as simple as 
possible so that anyone can extend the functionality without much complexity. 

Update the information you want to memorize into the memorize.txt file and run. This is the open source comand line version and there is a web version. 

Works with Python2.7 and 3.5 MacOS and Debian
Java version tested and works with IntelliJ
C++ version tested and works MacOS

Python Usage:
```
Open Terminal
git clone https://github.com/electronicsleep/FlashCards.git
cd FlashCards
python FlashCards.py
```

C++ Usage:
```
Open Terminal
git clone https://github.com/electronicsleep/FlashCards.git
cd FlashCards

#MacOS
llvm-g++ FlashCards.cpp -o ./FlashCards
#Linux
g++ FlashCards.cpp -o FlashCards

./FlashCards #run one
for i in {1..100}; do ./FlashCards; done #run drill one hundred
```

Python Command Line Version

![Screenshot CLI](screenshot-cli.jpg?raw=true "ScreenShot CLI")

Web Version

http://mathcard.us

![Screenshot Web](screenshot-web.jpg?raw=true "ScreenShot Web")

Java Version

![Screenshot Java](screenshot-java.jpg?raw=true "ScreenShot Java")


Todo/Ideas:
* Run the CreateMemFile.py script to generate times tables
* Modify the CreateMemFile.py to generate your own cards
* Remember last 3 cards to prevent duplicates
* Make cards for all different things
* Use as a todo application or terms list
* GUI interface for the cards using wxwidgets
* C++ version, Perl version, Bash version
* Loop in the main program with quit
* Stats on answered questions, time, topscore
* Save stats file save and load for future use
* Compete with others locally or on the net
* Website to post top scores via an API call
* iPhone version, Android version
* More math game ideas

Resources:
https://www.python.org/
