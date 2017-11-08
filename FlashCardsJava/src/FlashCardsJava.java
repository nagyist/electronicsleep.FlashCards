/*
 * Author: Chris Robertson https://github.com/electronicsleep
 * Date: 12/18/2016
 * Purpose: Open Source Application for learning and memorizing
 * Released under the BSD license
 *
 * Compilation:  javac FlashCardsJava.java
 * Execution:    java FlashCardsJava
 *
 *  % java FlashCardsJava
 */

import java.io.*;
import java.nio.charset.Charset;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class FlashCardsJava {

    public static void main(String[] args) throws IOException {
        // For CLI version
        System.out.println("FlashCardsJava");

        FlashCardsJava card_cli = new FlashCardsJava();
        card_cli.Card_CLI();
    }

    private void Card_CLI() {
        Card card_cli = new FlashCardsJava.Card();
        card_cli.getCard();

        //Print Question
        System.out.println(card_cli.cardReturn[0]);

        //Get Answer
        Scanner reader = new Scanner(System.in);
        System.out.println("What is the Answer: ");
        String n = reader.nextLine();
        System.out.println("Your Answer: " + n);
        String answer = card_cli.cardReturn[1].replace("A. ", "");
        System.out.println("Correct Answer: " + answer);
        if (answer.equals(n)) {
            System.out.println("You are correct");
        } else {
            System.out.println("You are incorrect");
        }
    }

    public class Card {
        //private String card;
        public String[] cardReturn = new String[2];

        public String getCard() {
            String filePath = "memorize.txt";

            //System.out.println("Memorize File: " + filePath);
            File file = new File(filePath);

            //System.out.println("File Exists: " + file.exists());

            int number_of_cards = 200;

            String[] Questions = new String[number_of_cards];
            String[] Answers = new String[number_of_cards];

            Random rand = new Random();
            int x = rand.nextInt(number_of_cards);

            if(file.exists()) {

                String line;
                int n = 0;

                try {
                    InputStream fis = new FileInputStream(filePath);
                    InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                    BufferedReader br = new BufferedReader(isr);

                    while ((line = br.readLine()) != null) {
                        //System.out.println("line: " + line);

                        if (n == number_of_cards) {
                            //System.out.println("Break: End of Array");
                            break;
                        }

                        if (line.startsWith("Q.")) {
                            //System.out.println("Found Question: " + line);
                            Questions[n] = line;
                        } else if (line.startsWith("A.")) {
                            //System.out.println("Found Answer: " + line);
                            Answers[n] = line;
                            n++;
                            //System.out.println("n: " + n);
                        }

                    }

                } catch (IOException e) {
                    e.printStackTrace();
                }

            } else {
                System.out.println("Can not find memorize.txt file!");
                System.exit(1);
            }
            cardReturn[0] = Questions[x];
            cardReturn[1] = Answers[x];

            String card = "\n" + Questions[x] + "\n" + Answers[x];
            return card;
        }
    }
}
