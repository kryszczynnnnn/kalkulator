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
    private int currentFontSize = 54;

    private JPanel historyPanel;

    public calculator() {
        setTitle("Kalkulator");
        setSize(800, 650);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        Color bg = new Color(54, 28, 8);
        Color btn = new Color(92, 61, 43);
        Color opBtn = new Color(106, 78, 60);
        Color eqBtn = new Color(230, 116, 35);
        Color textColor = Color.WHITE;

        JPanel root = new JPanel(new BorderLayout(12, 12));
        root.setBackground(bg);
        root.setBorder(BorderFactory.createEmptyBorder(12, 12, 12, 12));
        setContentPane(root);

        JPanel leftPanel = new JPanel(new BorderLayout(10, 10));
        leftPanel.setBackground(bg);

        JPanel displayPanel = new JPanel(new BorderLayout());
        displayPanel.setBackground(bg);

        historyDisplay = new JLabel(" ");
        historyDisplay.setForeground(Color.LIGHT_GRAY);
        historyDisplay.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        historyDisplay.setHorizontalAlignment(SwingConstants.RIGHT);

        mainDisplay = new JTextField("0");
        mainDisplay.setEditable(false);
        mainDisplay.setBorder(null);
        mainDisplay.setBackground(bg);
        mainDisplay.setForeground(textColor);
        mainDisplay.setFont(new Font("Segoe UI", Font.PLAIN, 54));
        mainDisplay.setHorizontalAlignment(JTextField.RIGHT);

        displayPanel.add(historyDisplay, BorderLayout.NORTH);
        displayPanel.add(mainDisplay, BorderLayout.CENTER);

        leftPanel.add(displayPanel, BorderLayout.NORTH);

        JPanel buttonsPanel = new JPanel(new GridLayout(6, 4, 8, 8));
        buttonsPanel.setBackground(bg);

        String[] buttons = {
                "%", "CE", "C", "<-",
                "1/x", "x²", "√x", "/",
                "7", "8", "9", "×",
                "4", "5", "6", "−",
                "1", "2", "3", "+",
                "+/-", "0", ",", "="
        };

        for (String text : buttons) {
            Color color = btn;
            if (text.equals("=")) color = eqBtn;
            else if (text.matches("[/×−+]")) color = opBtn;

            JButton b = new RoundedButton(text);
            b.setFont(new Font("Segoe UI", Font.BOLD, 20));
            b.setBackground(color);
            b.setForeground(textColor);
            b.setFocusPainted(false);
            b.setBorderPainted(false);
            b.setContentAreaFilled(false);
            b.setOpaque(false);
            b.addActionListener(e -> handleInput(text));
            buttonsPanel.add(b);
        }

        leftPanel.add(buttonsPanel, BorderLayout.CENTER);
        root.add(leftPanel, BorderLayout.CENTER);

        JPanel historyRoot = new JPanel(new BorderLayout(8, 8));
        historyRoot.setBackground(bg);

        JLabel historyTitle = new JLabel("History");
        historyTitle.setForeground(Color.WHITE);
        historyTitle.setFont(new Font("Segoe UI", Font.BOLD, 28));
        historyRoot.add(historyTitle, BorderLayout.NORTH);

        historyPanel = new JPanel();
        historyPanel.setLayout(new BoxLayout(historyPanel, BoxLayout.Y_AXIS));
        historyPanel.setBackground(bg);

        JScrollPane scroll = new JScrollPane(historyPanel);
        scroll.setBorder(BorderFactory.createLineBorder(Color.WHITE, 1));
        scroll.getViewport().setBackground(bg);
        scroll.setOpaque(false);

        historyRoot.add(scroll, BorderLayout.CENTER);
        historyRoot.setPreferredSize(new Dimension(260, 0));

        root.add(historyRoot, BorderLayout.EAST);

        setVisible(true);
    }

    private void adjustFontSizeToFit() {
    int w = mainDisplay.getWidth() - 20;  
    if (w <= 0) return;

    Font base = new Font("Segoe UI", Font.PLAIN, 54);
    int size = currentFontSize;
    FontMetrics fm;

    do {
        Font f = new Font(base.getName(), base.getStyle(), size);
        fm = mainDisplay.getFontMetrics(f);
        if (fm.stringWidth(mainDisplay.getText()) <= w) {
            break;
        }
        size--;
    } while (size > 12);

    currentFontSize = size;
    mainDisplay.setFont(new Font(base.getName(), base.getStyle(), currentFontSize));
    mainDisplay.revalidate();
    mainDisplay.repaint();
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
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals(",")) {
        if (!currentText.contains(",")) {
            mainDisplay.setText(currentText + ",");
            newInput = false;
        }
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("CE")) {
        mainDisplay.setText("0");
        newInput = true;
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("C")) {
        mainDisplay.setText("0");
        historyDisplay.setText(" ");
        firstNumber = 0;
        operator = "";
        newInput = true;
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("<-")) {
        if (currentText.length() > 1) {
            mainDisplay.setText(currentText.substring(0, currentText.length() - 1));
        } else {
            mainDisplay.setText("0");
            newInput = true;
        }
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("+/-")) {
        double val = parseDisplay(currentText);
        mainDisplay.setText(format(-val));
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("1/x")) {
        double val = parseDisplay(currentText);
        if (val == 0) {
            mainDisplay.setText("Error");
        } else {
            mainDisplay.setText(format(1.0 / val));
        }
        adjustFontSizeToFit();   
        return;
    }

    if (input.equals("x²")) {
        double val = parseDisplay(currentText);
        mainDisplay.setText(format(val * val));
        adjustFontSizeToFit();  
        return;
    }

    if (input.equals("√x")) {
        double val = parseDisplay(currentText);
        if (val < 0) {
            mainDisplay.setText("Error");
        } else {
            mainDisplay.setText(format(Math.sqrt(val)));
        }
        adjustFontSizeToFit();  
        return;
    }

    if (input.matches("[/×−+]")) {
        firstNumber = parseDisplay(currentText);
        operator = input;
        historyDisplay.setText(format(firstNumber) + " " + operator);
        newInput = true;
        mainDisplay.setText("0");
        adjustFontSizeToFit();  
        return;
    }

    if (input.equals("=")) {
        double secondNumber = parseDisplay(currentText);
        double result = 0;

        switch (operator) {
            case "+" -> result = firstNumber + secondNumber;
            case "−" -> result = firstNumber - secondNumber;
            case "×" -> result = firstNumber * secondNumber;
            case "/" -> {
                if (secondNumber == 0) {
                    mainDisplay.setText("Error");
                    adjustFontSizeToFit();   
                    return;
                }
                result = firstNumber / secondNumber;
            }
        }

        String equation = format(firstNumber) + " " + operator + " " + format(secondNumber) + " = " + format(result);
        addToHistory(equation, result);

        mainDisplay.setText(format(result));
        historyDisplay.setText(" ");
        newInput = true;
        adjustFontSizeToFit();   
    }
}

    private void addToHistory(String equation, double result) {
        JButton btn = new RoundedButton(equation);
        btn.setAlignmentX(Component.LEFT_ALIGNMENT);
        btn.setMaximumSize(new Dimension(240, 55));
        btn.setPreferredSize(new Dimension(240, 55));
        btn.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        btn.setForeground(Color.WHITE);
        btn.setBackground(new Color(92, 61, 43));
        btn.setFocusPainted(false);
        btn.setBorderPainted(false);
        btn.setContentAreaFilled(false);
        btn.setOpaque(false);
        btn.addActionListener(e -> mainDisplay.setText(format(result)));

        historyPanel.add(Box.createVerticalStrut(8));
        historyPanel.add(btn);
        historyPanel.revalidate();
        historyPanel.repaint();
    }

    private double parseDisplay(String text) {
        return Double.parseDouble(text.replace(",", "."));
    }

    private String format(double value) {
        if (value == (long) value) return String.valueOf((long) value);
        return String.valueOf(value).replace(".", ",");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(calculator::new);
    }

    class RoundedButton extends JButton {
        public RoundedButton(String text) {
            super(text);
            setMargin(new Insets(10, 10, 10, 10));
        }

        @Override
        protected void paintComponent(Graphics g) {
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setColor(getBackground());
            g2.fillRoundRect(0, 0, getWidth(), getHeight(), 20, 20);
            super.paintComponent(g);
            g2.dispose();
        }

        @Override
        protected void paintBorder(Graphics g) {
        }

        @Override
        public boolean isContentAreaFilled() {
            return false;
        }
    }
}