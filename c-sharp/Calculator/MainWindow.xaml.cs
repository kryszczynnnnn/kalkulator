// Author of this code and program is Serhii Skyba

using System.IO;
using System.Media;
using System.Printing;
using System.Reflection;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Calculator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    
    public partial class MainWindow : Window
    {
        // Predefined Variables

        private string buttonNumber; // Used for identifying, what number button is pressed

        private string FunctionType; // Used for remembering, which function was selected

        private string Wpisane = ""; // Used to take data from calculator field and data manipulation

        private double NumberOne; // Used for remembering first number after pressing function button

        private double NumberTwo; // Used for remembering second number after pressing equals button

        private double Calc; // Used for counting final result

        // Used for playing sound, when clicking the button
        
        public MainWindow()
        {
            InitializeComponent();
            
        }
        
        // Used for entering numbers through GUI
        private void Wpisz(object sender, RoutedEventArgs e)
        {
            buttonNumber = $"{((Button)sender).Content}";

            if (inputbox.Text == "NaN" || inputbox.Text == "∞")
                inputbox.Text = "0";

            Wpisane = inputbox.Text;

            if (Wpisane == "0")
            {
                if (buttonNumber == ",")
                    Wpisane = "0";
                else
                    Wpisane = "";
            }

            if (Wpisane.Contains(",") && buttonNumber == ",")
                buttonNumber = "";

            Wpisane += buttonNumber;
            inputbox.Text = Wpisane;

            // Used for displaying supossed result, if FunctionType has value
            if (FunctionType == "+" || FunctionType == "-" || FunctionType == "/" || FunctionType == "*" || FunctionType == "^" || FunctionType == "log")
            {
                NumberTwo = double.Parse(inputbox.Text);
                switch (FunctionType)
                {
                    case "+":
                        Calc = NumberOne + NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "-":
                        Calc = NumberOne - NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "/":
                        Calc = NumberOne / NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "*":
                        Calc = NumberOne * NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "^":
                        Calc = Math.Pow(NumberOne, NumberTwo);
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "log":
                        Calc = Math.Log(NumberOne, NumberTwo);
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                }
                if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                    result.Text = "0";
            }
            else
                result.Text = "";
            Wpisane = "";
        }

        // Clears calculator field and all variables
        private void Clear(object sender, RoutedEventArgs e)
        {
            inputbox.Text = "0";
            result.Text = "";
            FunctionType = "";
            Wpisane = "";
            NumberOne = 0;
            NumberTwo = 0;
        }

        // Used for errasign last digit
        private void Erase(object sender, RoutedEventArgs e)
        {
            Wpisane = inputbox.Text;
            if (Wpisane != "")
                Wpisane = Wpisane.Remove(Wpisane.Length - 1, 1);
            if (Wpisane == "")
                Wpisane = "0";
            inputbox.Text = Wpisane;

            // Used for displaying supossed result, if FunctionType has value
            if (FunctionType == "+" || FunctionType == "-" || FunctionType == "/" || FunctionType == "*" || FunctionType == "^" || FunctionType == "log")
            {
                NumberTwo = double.Parse(inputbox.Text);
                switch (FunctionType)
                {
                    case "+":
                        Calc = NumberOne + NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "-":
                        Calc = NumberOne - NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "/":
                        Calc = NumberOne / NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "*":
                        Calc = NumberOne * NumberTwo;
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "^":
                        Calc = Math.Pow(NumberOne, NumberTwo);
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                    case "log":
                        Calc = Math.Log(NumberOne, NumberTwo);
                        Wpisane = Calc.ToString();
                        result.Text = Wpisane;
                        break;
                }
                if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                    result.Text = "0";
            }
            else
                result.Text = "";
        }

        // Swaps value of entered number from positive to negative and vice versa
        private void Swap(object sender, RoutedEventArgs e)
        {
            Wpisane = inputbox.Text;
            if (Wpisane.Contains("-") == true)
                Wpisane = Wpisane.Replace("-", "");
            else
                Wpisane = "-" + Wpisane;
            inputbox.Text = Wpisane;
        }

        // Defines, what operation type is entered
        private void Function(object sender, RoutedEventArgs e)
        {
            FunctionType = $"{((Button)sender).Content}";
            NumberOne = double.Parse(inputbox.Text); // Sets value of first number to value of calculator field with convertation
            inputbox.Text = "0";
        }

        // Calculates root of number
        private void Root(object sender, RoutedEventArgs e)
        {
            NumberOne = double.Parse(inputbox.Text);
            NumberOne = Math.Sqrt(NumberOne);
            inputbox.Text = NumberOne.ToString();
        }

        // Calculates cubic root of number
        private void CubicRoot(object sender, RoutedEventArgs e)
        {
            NumberOne = double.Parse(inputbox.Text);
            NumberOne = Math.Cbrt(NumberOne);
            inputbox.Text = NumberOne.ToString();
        }

        // Calculates factorial of a number
        private void Factorial(object sender, RoutedEventArgs e)
        {
            NumberOne = double.Parse(inputbox.Text);
            int factorial = 1;
            for (int i = 1; i <= NumberOne; i++)
            {
                factorial = factorial * i;
            }
            inputbox.Text = factorial.ToString();
        }

        // Calculates final result
        private void Calculate(object sender, RoutedEventArgs e)
        {
            NumberTwo = double.Parse(inputbox.Text);
            result.Text = "";
            
            // Depending on value of FunctionType, calculates final result using two numbers
            switch (FunctionType)
            {
                case "+":
                    Calc = NumberOne + NumberTwo;
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                case "-":
                    Calc = NumberOne - NumberTwo;
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                case "/":
                    Calc = NumberOne / NumberTwo;
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                case "*":
                    Calc = NumberOne * NumberTwo;
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                case "^":
                    Calc = Math.Pow(NumberOne, NumberTwo);
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                case "log":
                    Calc = Math.Log(NumberOne, NumberTwo);
                    Wpisane = Calc.ToString();
                    inputbox.Text = Wpisane;
                    FunctionType = "";
                    break;
                default:
                    inputbox.Text = Calc.ToString();
                    if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                        inputbox.Text = "0";
                    break;
            }
            if (inputbox.Text == "Nan" || inputbox.Text == "NaN" || inputbox.Text == "∞")
                inputbox.Text = "0";
        }

        // Those are keybindings, they are use this program using only keyboard
        private void Window_Keys(object sender, KeyEventArgs e)
        {
            string PressedKey = e.Key.ToString(); // Checks, which key was pressed

            // If the key is number or numpad number, enters this into calculator field
            if (PressedKey == "D1" || PressedKey == "D2" || PressedKey == "D3" || PressedKey == "D4" || PressedKey == "D5" || PressedKey == "D6" || PressedKey == "D7" || PressedKey == "D8" || PressedKey == "D9" || PressedKey == "D0" || PressedKey == "NumPad1" || PressedKey == "NumPad2" || PressedKey == "NumPad3" || PressedKey == "NumPad4" || PressedKey == "NumPad5" || PressedKey == "NumPad6" || PressedKey == "NumPad7" || PressedKey == "NumPad8" || PressedKey == "NumPad9" || PressedKey == "NumPad0")
            {
                // Checks, if key is number or numpad number
                if (PressedKey == "D1" || PressedKey == "D2" || PressedKey == "D3" || PressedKey == "D4" || PressedKey == "D5" || PressedKey == "D6" || PressedKey == "D7" || PressedKey == "D8" || PressedKey == "D9" || PressedKey == "D0")
                    PressedKey = PressedKey.Replace("D", "");
                else
                    PressedKey = PressedKey.Replace("NumPad", "");

                if (inputbox.Text == "0")
                    inputbox.Text = "";
                if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                    inputbox.Text = "0";
                Wpisane = inputbox.Text;
                Wpisane = Wpisane + PressedKey;
                inputbox.Text = Wpisane;
                if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                    inputbox.Text = "0";

                // Used for displaying supossed result, if FunctionType has value
                if (FunctionType == "+" || FunctionType == "-" || FunctionType == "/" || FunctionType == "*" || FunctionType == "^" || FunctionType == "log")
                {
                    NumberTwo = double.Parse(inputbox.Text);
                    switch (FunctionType)
                    {
                        case "+":
                            Calc = NumberOne + NumberTwo;
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                        case "-":
                            Calc = NumberOne - NumberTwo;
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                        case "/":
                            Calc = NumberOne / NumberTwo;
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                        case "*":
                            Calc = NumberOne * NumberTwo;
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                        case "^":
                            Calc = Math.Pow(NumberOne, NumberTwo);
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                        case "log":
                            Calc = Math.Log(NumberOne, NumberTwo);
                            Wpisane = Calc.ToString();
                            result.Text = Wpisane;
                            break;
                    }
                    if (Wpisane == "Nan" || Wpisane == "NaN" || Wpisane == "∞")
                        result.Text = "0";
                }
            }
            // If the key is operator, changes FunctionType depending on key
            if (PressedKey == "Add" || PressedKey == "Divide" || PressedKey == "Subtract" || PressedKey == "Multiply" || PressedKey == "P" || PressedKey == "L")
            {
                switch (PressedKey) {
                    case "Add":
                        FunctionType = "+";
                        break;
                    case "Divide":
                        FunctionType = "/";
                        break;
                    case "Subtract":
                        FunctionType = "-";
                        break;
                    case "Multiply":
                        FunctionType = "*";
                        break;
                    case "P":
                        FunctionType = "^";
                        break;
                    case "L":
                        FunctionType = "log";
                        break;
                }
                NumberOne = double.Parse(inputbox.Text);
                inputbox.Text = "0";
            }

            // Used for other keybindings
            switch (PressedKey)
            {
                // Works like Calculate function but only when you press Enter (Return)
                case "Return":
                    NumberTwo = double.Parse(inputbox.Text);
                    switch (FunctionType)
                    {
                        case "+":
                            Calc = NumberOne + NumberTwo;
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        case "-":
                            Calc = NumberOne - NumberTwo;
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        case "/":
                            Calc = NumberOne / NumberTwo;
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        case "*":
                            Calc = NumberOne * NumberTwo;
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        case "^":
                            Calc = Math.Pow(NumberOne, NumberTwo);
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        case "log":
                            Calc = Math.Log(NumberOne, NumberTwo);
                            Wpisane = Calc.ToString();
                            inputbox.Text = Wpisane;
                            NumberOne = Calc;
                            result.Text = "";
                            FunctionType = "";
                            break;
                        default:
                            inputbox.Text = Calc.ToString();
                            break;
                    }
                    if (inputbox.Text == "Nan" || inputbox.Text == "NaN" || inputbox.Text == "∞")
                        inputbox.Text = "0";
                break;

                // Works like Clear function but only when you press C
                case "C":
                    inputbox.Text = "0";
                    result.Text = "";
                    Wpisane = "";
                    NumberOne = 0;
                    NumberTwo = 0;
                    break;

                // Works like Erase function but only when you press BackSpace (Back)
                case "Back":
                    Wpisane = inputbox.Text;
                    if (Wpisane != "")
                        Wpisane = Wpisane.Remove(Wpisane.Length - 1, 1);
                    if (Wpisane == "")
                        Wpisane = "0";
                    inputbox.Text = Wpisane;
                    break;

                // Works like Swap function but only when you press S
                case "S":
                    Wpisane = inputbox.Text;
                    if (Wpisane.Contains("-") == true)
                        Wpisane = Wpisane.Replace("-", "");
                    else
                        Wpisane = "-" + Wpisane;
                    inputbox.Text = Wpisane;
                    break;

                // Works like Root function but only when you press R
                case "R":
                    NumberOne = double.Parse(inputbox.Text);
                    NumberOne = Math.Sqrt(NumberOne);
                    inputbox.Text = NumberOne.ToString();
                    break;

                // Works like CubicRoot function but only when you press T
                case "T":
                    NumberOne = double.Parse(inputbox.Text);
                    NumberOne = Math.Cbrt(NumberOne);
                    inputbox.Text = NumberOne.ToString();
                    break;

                // Works like Factorial function but only when you press F
                case "F":
                    NumberOne = double.Parse(inputbox.Text);
                    int factorial = 1;
                    for (int i = 1; i <= NumberOne; i++)
                    {
                        factorial = factorial * i;
                    }
                    inputbox.Text = factorial.ToString();
                    break;

                // Works like Wpisz function but only for decimal (,) and only when you press Decimal (,)
                case "Decimal":
                    buttonNumber = ",";
                    if (inputbox.Text == "0" && buttonNumber != ",")
                        inputbox.Text = "";
                    Wpisane = inputbox.Text;
                    if (Wpisane.Contains(",") == true && buttonNumber == ",")
                    {
                        buttonNumber = "";
                    }
                    Wpisane = Wpisane + buttonNumber;
                    inputbox.Text = Wpisane;
                    break;
            }
        }
    }
}