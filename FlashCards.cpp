/*
Author: Chris Robertson <electronicsleep@gmail.com>
Date: 12/11/2016
Purpose: Simple FlashCard app for learning math and C++
Released under the BSD license

Running:
g++ FlashCards.cpp -o FlashCards
./FlashCards
*/

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <unistd.h>
#include <stdlib.h>

using namespace std;

int main () 
{
  string text;
  ifstream ifs("memorize.txt");

  int num = 0;
  int card = 0;


  std::vector<std::string> answers;
  std::vector<std::string> questions;

    while(!ifs.eof()) 
    {
      getline(ifs, text);

      //cout << "LINE: " << num << " " << text << "\n" ;

      if (text.find("Q.") != std::string::npos) {
        //cout << "found Question Card" << '\n';
        questions.push_back(string(text));
      } else if (text.find("A.") != std::string::npos) {
        //cout << "found Answer Card" << '\n';
        answers.push_back(string(text));
        num++;
      }

    }

  //Get random card
  srand(time(NULL));
  card = rand() % num; 
  
  cout << "Number of Cards: " << num << endl;

  //Show random card
  cout << "=======-----Random Card-----=======" << endl;
  cout << "Question: " << questions[card] << endl;
  usleep(3000000); 
  cout << "Answer: " << answers[card] << endl;
  cout << "-----------------------------------" << endl;

  return 0;
}
