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

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class app {
    private JPanel panel1;
    private JButton button1;

    public app() {
        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "FlashCards.");
            }
        });
    }

    public static void main(String[] args) {
      JFrame frame = new JFrame("app");
        frame.setContentPane(new app().panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
