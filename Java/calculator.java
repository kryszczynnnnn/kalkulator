import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class calculator extends JFrame {

    private JTextField mainDisplay;
    private JLabel historyDisplay;

    private double firstNumber = 0;
    private String operator = "";
    private boolean newInput = true;

    private ArrayList<String> history = new ArrayList<>();
    private JPanel historyPanel;

    public calculator() {
        setTitle("Kalkulator");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // dispaly 
        JPanel displayPanel = new JPanel(new GridLayout(2,1));

        historyDisplay = new JLabel("");
        historyDisplay.setFont(new Font("Arial", Font.PLAIN, 16));
        historyDisplay.setHorizontalAlignment(SwingConstants.RIGHT);

        mainDisplay = new JTextField("0");
        mainDisplay.setFont(new Font("Arial", Font.BOLD, 28));
        mainDisplay.setHorizontalAlignment(JTextField.RIGHT);

        displayPanel.add(historyDisplay);
        displayPanel.add(mainDisplay);

        add(displayPanel, BorderLayout.NORTH);

        // przyckksi
        JPanel panel = new JPanel(new GridLayout(5, 4));

        String[] buttons = {
                "C", "+/-", "%", "/",
                "7", "8", "9", "*",
                "4", "5", "6", "-",
                "1", "2", "3", "+",
                "0", "x²", "√", "="
        };

        for (String text : buttons) {
            JButton btn = new JButton(text);
            btn.setFont(new Font("Arial", Font.BOLD, 18));
            panel.add(btn);

            btn.addActionListener(e -> handleInput(text));
        }

        add(panel, BorderLayout.CENTER);

        // historia rownan
        historyPanel = new JPanel();
        historyPanel.setLayout(new BoxLayout(historyPanel, BoxLayout.Y_AXIS));

        JScrollPane scroll = new JScrollPane(historyPanel);
        scroll.setPreferredSize(new Dimension(400, 150));

        add(scroll, BorderLayout.SOUTH);

        setVisible(true);
    }

    private void handleInput(String input) {

        String currentText = mainDisplay.getText();

        if (input.matches("[0-9]")) {
            if (newInput || currentText.equals("0")) {
                mainDisplay.setText(input);
                newInput = false;
            } else {
                mainDisplay.setText(currentText + input);
            }
            return;
        }

        // clear
        if (input.equals("C")) {
            mainDisplay.setText("0");
            historyDisplay.setText("");
            firstNumber = 0;
            operator = "";
            return;
        }

        // plus/minus
        if (input.equals("+/-")) {
            double val = Double.parseDouble(mainDisplay.getText());
            val *= -1;
            mainDisplay.setText(String.valueOf(val));
            return;
        }

        // procent
        if (input.equals("%")) {
            double val = Double.parseDouble(mainDisplay.getText());
            val = firstNumber * val / 100;
            mainDisplay.setText(String.valueOf(val));
            return;
        }

        // pierwiastek
        if (input.equals("√")) {
            double val = Double.parseDouble(mainDisplay.getText());
            val = Math.sqrt(val);
            mainDisplay.setText(String.valueOf(val));
            return;
        }

        // do kwadratu
        if (input.equals("x²")) {
            double val = Double.parseDouble(mainDisplay.getText());
            val = val * val;
            mainDisplay.setText(String.valueOf(val));
            return;
        }

        // x przez 1
        if (input.equals("1/x")) {
            double val = Double.parseDouble(mainDisplay.getText());
            val = 1 / val;
            mainDisplay.setText(String.valueOf(val));
            return;
        }

        // operatory
        if (input.matches("[+\\-*/]")) {
            firstNumber = Double.parseDouble(mainDisplay.getText());
            operator = input;

            historyDisplay.setText(firstNumber + " " + operator);

            mainDisplay.setText("0");
            newInput = true;
            return;
        }

        // rowna sie
        if (input.equals("=")) {
            double secondNumber = Double.parseDouble(mainDisplay.getText());
            double result = 0;

            switch (operator) {
                case "+":
                    result = firstNumber + secondNumber;
                    break;
                case "-":
                    result = firstNumber - secondNumber;
                    break;
                case "*":
                    result = firstNumber * secondNumber;
                    break;
                case "/":
                    if (secondNumber == 0) {
                        mainDisplay.setText("Error");
                        return;
                    }
                    result = firstNumber / secondNumber;
                    break;
            }

            String equation = firstNumber + " " + operator + " " + secondNumber + " = " + result;

            addToHistory(equation, result);

            mainDisplay.setText(String.valueOf(result));
            historyDisplay.setText("");
            newInput = true;
        }
    }

    private void addToHistory(String equation, double result) {

        JButton btn = new JButton(equation);
        btn.setMaximumSize(new Dimension(350, 30));

        btn.addActionListener(e -> {
            mainDisplay.setText(String.valueOf(result));
        });

        historyPanel.add(btn);
        historyPanel.revalidate();
    }

    public static void main(String[] args) {
        new calculator();
    }
}