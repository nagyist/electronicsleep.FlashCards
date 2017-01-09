/******************************************************************************
 * Author: Chris Robertson <electronicsleep@gmail.com>
 * Date: 12/18/2016
 * Purpose: Open Source Application for learning and memorizing
 * Released under the BSD license
 *
 * Compilation:  javac FlashCardsJava.java
 * Execution:    java FlashCardsJava
 *
 *  % java FlashCardsJava
 ******************************************************************************/

import java.io.*;
import java.nio.charset.Charset;
import java.io.IOException;
import java.util.Random;

public class FlashCardsJava {


    public static void main(String[] args) throws IOException {

        // For CLI version
        System.out.println("Hello FlashCards");

        //Card card_cli = new Card();
        //System.out.println("card: " + card_cli);
    }

    public class Card {

        public String card;


        public String Card(String card) {
            this.card = card;
            return card;
        }

        public String toString() {
            //card = "Hello...";

            String path = "memorize.txt";

            System.out.println(path);
            File file = new File(path);

            System.out.println(file.exists());

            int number_of_cards = 200;

            String[] Questions = new String[number_of_cards];
            String[] Answers = new String[number_of_cards];

            Random rand = new Random();
            int x = rand.nextInt(number_of_cards);

            if(file.exists()) {

                String line;
                int n = 0;

                try {
                    InputStream fis = new FileInputStream(path);
                    InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                    BufferedReader br = new BufferedReader(isr);

                    while ((line = br.readLine()) != null) {
                        //System.out.println("line: " + line);

                        if (n == number_of_cards) {
                            System.out.println("Break: End of Array");
                            break;
                        }

                        if (line.startsWith("Q.")) {
                            System.out.println("Found Question: " + line);
                            Questions[n] = line;
                        } else if (line.startsWith("A.")) {
                            System.out.println("Found Answer: " + line);
                            Answers[n] = line;
                            n++;
                            System.out.println("n: " + n);
                        }

                    }

                } catch (IOException e) {
                    e.printStackTrace();
                }

                System.out.println("Random num:" + x);

                System.out.println(Questions[x]);

                //try {
                //    Thread.sleep(3000);
                //} catch(InterruptedException ex) {
                //    Thread.currentThread().interrupt();
                //}

                System.out.println(Answers[x]);

            } else {
                System.out.println("Can not find memorize.txt file!");
            }
            card = "\n" + Questions[x] + "\n" + Answers[x];

            return card;
        }

    }



}
