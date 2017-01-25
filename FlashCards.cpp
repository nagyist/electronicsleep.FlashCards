/*
Author: Chris Robertson <electronicsleep@gmail.com>
Date: 12/11/2016
Purpose: Simple FlashCard app for learning math and C++
Released under the BSD license

Running:
llvm-g++ FlashCards.cpp -o ./FlashCards
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


bool does_file_exist(string fileName)
{
    std::ifstream infile(fileName);
    return infile.good();
}

int main () 
{

  string mem_file = "memorize.txt";
 
    

  if (!does_file_exist(mem_file))
  {
  cout << mem_file + " file does not exist: " << endl;
  return 1;
  } else {
  cout << "Using Memory File:" + mem_file;

  

  string text;
  ifstream ifs(mem_file);

  int num = 0;
  int card = 0;


  std::vector<std::string> answers;
  std::vector<std::string> questions;

    while(!ifs.eof()) 
    {
      getline(ifs, text);

      if (text.find("Q.") != std::string::npos) {
        questions.push_back(string(text));
      } else if (text.find("A.") != std::string::npos) {
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
}


