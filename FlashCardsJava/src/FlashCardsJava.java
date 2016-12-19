/******************************************************************************
 * Author: Chris Robertson <electronicsleep@gmail.com>
 * Date: 12/18/2016
 * Purpose: Simple FlashCard app for learning math and Java
 * Released under the BSD license
 *
 * Compilation:  javac MathCardsJava.java
 * Execution:    java MathCardsJava.java
 *
 *  % java FlashCardsJava.java
 ******************************************************************************/

import java.io.*;
import java.nio.charset.Charset;
import java.io.IOException;

public class FlashCardsJava {

    public static void main(String[] args) throws IOException {
        System.out.println("FlashCards");

        String path = "memorize.txt";

        System.out.println(path);
        File file = new File(path);

        System.out.println(file.exists());

        if(file.exists()) {

            String[] Questions = new String[20];
            String[] Answers = new String[20];

            String line;
            try {
                InputStream fis = new FileInputStream(path);
                InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                BufferedReader br = new BufferedReader(isr);

                while ((line = br.readLine()) != null) {
                    //System.out.println("line:" + line);

                    if (line.startsWith("Q.")) {
                        //System.out.println("Found Question");
                        Questions[0] = line;
                    } else if (line.startsWith("A.")) {
                        //System.out.println("Found Answer");
                        Answers[0] = line;
                    }
                }

            } catch (IOException e) {
                e.printStackTrace();
            }

        System.out.println(Questions[0]);
        System.out.println(Answers[0]);
        }

    }
}