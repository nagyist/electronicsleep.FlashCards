#!/bin/bash
set -e
echo "Build FlashCards Java"
cd src
javac FlashCardsJava.java
java FlashCardsJava
echo "Java Build OK"
