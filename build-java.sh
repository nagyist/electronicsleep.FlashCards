#!/bin/bash
set -e
echo "Build FlashCards Java"
#git clone https://github.com/electronicsleep/FlashCards.git
cd FlashCardsJava/src
javac FlashCardsJava.java
java FlashCardsJava
echo "Java Build OK"
