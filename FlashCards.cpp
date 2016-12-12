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
#include <string>
#include <cstring>
#include <time.h>
#include <unistd.h>

using namespace std;

int main () 
{
  string text;
  ifstream ifs("memorize.txt");


  int num = 0;
  int card = 0;

  string answers[50];
  string questions[50];

    while(!ifs.eof()) 
    {
      getline(ifs, text);


      //cout << "LINE: " << num << " " << text << "\n" ;

      if (text.find("Q.") != std::string::npos) {
        //cout << "found Question Card" << '\n';
        questions[num] = string(text);
      } else if (text.find("A.") != std::string::npos) {
        //cout << "found Answer Card" << '\n';
        answers[num] = string(text);
        num++;

        if (num >= 50) {
          break;
        }

      }

    }

  //Get random card
  srand(time(NULL));
  card = rand() % num; 
  
  cout << "Random Num: " << card << endl;
  cout << "Number of Cards: " << num << endl;

  //Show random card
  cout << "Random Card: " << endl;
  cout << "Question: " << questions[card] << endl;
  usleep(3000000); 
  cout << "Answer: " << answers[card] << endl;

  return 0;
}
