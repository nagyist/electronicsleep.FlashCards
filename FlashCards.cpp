/*
Author: Chris Robertson <electronicsleep@gmail.com>
Date: 12/11/2016
Purpose: Simple FlashCard app for learning math and C++
Released under the BSD license

Running:
cppcheck FlashCards.cpp
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


int main(int argc, char** argv)
{

  string mem_file = "memorize.txt";
  string answer = "";
  string text = "";

  if (!does_file_exist(mem_file))
  {
  cout << mem_file + " file does not exist" << endl;
  return 1;
  } else {
  cout << "Using Memory File: " + mem_file << endl;

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

    if (num == 0)
    {
      cout << "No cards in " + mem_file + " file" << endl;
      return 0;
    } 

 
  cout << "Number of Cards: " << num << endl;

  int x = 0;
  int num_correct = 0;
  int num_incorrect = 0;

  for (x = 0; x < 100; x++) {

    //Get random card
    srand(time(NULL));
    card = rand() % num; 
 
    //Show random card
    cout << "/=======-----===========-----=======/" << endl;
    cout << "/=======-----Random Card-----=======/" << endl;
    cout << "Question: " << questions[card] << endl;
    //usleep(3000000); 

    cout << "Enter Answer: "; 

    cin >> answer;

    //cout << answers[card] << endl;
    //cout << answer << endl;

    if (answers[card] == ("A. " + answer)) {
      cout << "Correct" << endl;
      num_correct++;
    } else {
      cout << "Incorrect" << endl;
      num_incorrect++;
    }

    cout << "Answer: " << answers[card] << endl;
    cout << "-----------------------------------=/" << endl;
    cout << " -----------===========-----------=//" << endl;
    printf ("Num correct: %d Num incorrect: %d\n\n", num_correct, num_incorrect);
  }

  return 0;
  }
}
