# Program was written by Serhii Skyba

# IMPORTING REQUIRED LIBRARIES AND VARIABLES
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QGridLayout, QGroupBox, QDialog, QScrollArea, QSlider
from PyQt5.QtGui import QIcon
import math
from style import QSS
import sys

# GLOBAL VARIABLES
temp_type = ""         # Stores the type of last operator used
is_inserted = False    # Checks, if 
liczba1 = ""           # Writes down the number before adding operator
liczba2 = ""           # Writes down the number after adding operator
history = []           # Writes down all calculations done in that session
id_counter = 0         # Gives an ID for a history item

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setStyleSheet(QSS)
        self.initUI()
    
    # Generating UI for a window    
    def initUI(self):
        self.calculator()
        
        # Creates a label for displaying current operation
        self.wyliczone = QLabel("", objectName="wyliczone")
        self.wyliczone.setAlignment(Qt.AlignRight)
        
        # Creates a label for displaying and storing current variable data (Used to paste info into liczba1 and liczba2)
        self.wpis = QLabel("0", objectName="wpis")
        self.wpis.setAlignment(Qt.AlignRight)
        
        # Creating a history widget
        history_widget_wrapper = QVBoxLayout(objectName = "scroll_widget")
        history_widget_label = QLabel("Historia Obliczeń")
        
        self.history_layout = QVBoxLayout(objectName = "scroll_widget")
        self.history_layout.setAlignment(Qt.AlignTop)
        history_widget = QWidget(objectName = "scroll_widget")
        
        # Defining a scroll wrapper for a history widget
        history_widget_scroll_wrapper = QScrollArea()
        
        history_widget_scroll_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        history_widget_scroll_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        history_widget_scroll_wrapper.setWidgetResizable(True)
        
        history_widget.setLayout(self.history_layout)
        history_widget_scroll_wrapper.setWidget(history_widget)
        history_widget_wrapper.setAlignment(Qt.AlignTop)
        history_widget_wrapper.addWidget(history_widget_label)
        history_widget_wrapper.addWidget(history_widget_scroll_wrapper)
        
        # Adding all calculator widget to the calculator layout
        calculator_layout = QVBoxLayout()
        calculator_layout.addWidget(self.wyliczone)
        calculator_layout.addWidget(self.wpis)
        calculator_layout.addWidget(self.button_group)
        
        # Adding all widgets to one layout
        windowLayout = QHBoxLayout()
        windowLayout.addLayout(calculator_layout)
        windowLayout.addLayout(history_widget_wrapper)
        self.setLayout(windowLayout)
        
        self.show()    
    
    # DEFINING THE GUI FOR CALCULATOR ITSELF
    def calculator(self):
        
        # Defining button wrapper
        self.button_group = QGroupBox(objectName="guziki_wrapper")
        layout = QGridLayout(objectName="guziki")
        #layout.setColumnStretch(1, 3)
        #layout.setColumnStretch(2, 4)
        
        # Creating first row of buttons
        # - Creating % button, which divides number by 100
        percent_button = QPushButton(text="%", objectName="operation_button")
        percent_button.clicked.connect(lambda:self.operation(type="%"))
        layout.addWidget(percent_button, 0, 0)
        
        # - Creating clear all button, which clears all the values
        clear_all_button = QPushButton(text="CE", objectName="delete_button")
        clear_all_button.clicked.connect(self.clear_all)
        layout.addWidget(clear_all_button, 0, 1)
        
        # - Creating clear button, which clears all the values
        clear_button = QPushButton(text="C", objectName="delete_button")
        clear_button.clicked.connect(self.clear)
        layout.addWidget(clear_button, 0, 2)
        
        # - Creating a delete button, which deletes last entered character
        delete_button = QPushButton(text="<-", objectName="delete_button")
        delete_button.clicked.connect(self.delete)
        layout.addWidget(delete_button, 0, 3)
        
        # Creating second row of buttons
        # - Creating a 1/X button, which divides 1 by the currently entered number
        ulamek_button = QPushButton(text="1/X", objectName="operation_button")
        ulamek_button.clicked.connect(lambda:self.operation(type="1/X"))
        layout.addWidget(ulamek_button, 1, 0)
        
        # - Creating a square root button, which finds out a root of an entered number
        square_root_button = QPushButton(text="√X", objectName="operation_button")
        square_root_button.clicked.connect(lambda:self.operation(type="root"))
        layout.addWidget(square_root_button, 1, 1)
        
        # - Creating a power of 2 button, which multiplyes current value by itself
        power_button = QPushButton(text="X²", objectName="operation_button")
        power_button.clicked.connect(lambda:self.operation(type="power"))
        layout.addWidget(power_button, 1, 2)
        
        # Defining main calculation sumbols
        operation_symbols=["/", "*", "+", "-"]
        
        # Mass producing operation buttons, based on the operation symbols in the table above
        # Those cover last column of rows from 2 to 5
        for i in range(1, len(operation_symbols)+1):
            symbol = operation_symbols[i-1]
            button = QPushButton(text=symbol, objectName="operation_button")
            button.clicked.connect(lambda _, t=button.text(): self.operation(type=t))
            layout.addWidget(button, i, 3)
        
        # Mass producing number buttons from 1 to 9
        # Those cover first three columns in the rows from 2 to 5
        for i in range(2,5):
            for j in range(0, 3):
                button = QPushButton(text=str(j+(i-2)*3+1))
                button.clicked.connect(lambda _, t=button.text(): self.enter(letter=t))
                layout.addWidget(button, i, j)
                
        # Creating sixth row of buttons
        # - Creating a +/- button, which turns value of current number to the oposite one
        reverse_button = QPushButton(text="+/-", objectName="operation_button")
        reverse_button.clicked.connect(lambda:self.operation(type="reverse"))
        layout.addWidget(reverse_button, 6, 0)
        
        # - Creating a 0 button, which would add 0 to the user number
        zero_button = QPushButton(text="0")
        zero_button.clicked.connect(lambda:self.enter(zero_button.text()))
        layout.addWidget(zero_button, 6, 1)
        
        # - Creating a . button, which would add . to the user number
        dot_button = QPushButton(text=".")
        dot_button.clicked.connect(lambda:self.enter(dot_button.text()))
        layout.addWidget(dot_button, 6, 2)
        
        # - Creating a = button, which would apply the equasion
        equals_button = QPushButton(text="=", objectName="equals_button")
        equals_button.clicked.connect(lambda:self.operation(type=equals_button.text()))
        layout.addWidget(equals_button, 6, 3)
        
        # Exporting layout
        self.button_group.setLayout(layout)
        
    # DEFINING FUNCTION, WHICH ADDS OPERATIONS DONE BY USER INTO LIST
    def add_history_item(self, rownanie, result):
        
        # Importing global variables
        global temp_type, is_inserted, liczba1, liczba2, id_counter
        id = id_counter
        
        # Defining history button, which would have a unique id with coresponding user action
        history_button = QPushButton(text = rownanie+result, objectName="history_button")
        history_button.clicked.connect(lambda _, t=history_button.text(): self.history_item_action(id))
        self.history_layout.addWidget(history_button)
        
        # Adding new item to the list of history items
        # - Each history item will have a following subitems:
        # -- temp_type = operation type
        # -- is_inserted = checks, if the number should to be replaced on entering new number or not
        # -- liczba1 = first number of the operation
        # -- liczba2 = second number of the operation
        # -- rownanie = final equasion
        history.append([temp_type, is_inserted, liczba1, liczba2, rownanie])
        id_counter = id_counter + 1
        
    # DEFINING FUNCTION, WHICH INNACTS HISTORY ITEM
    def history_item_action(self, id):
        
        # Importing global variables
        global temp_type, is_inserted, liczba1, liczba2, history
        
        # Assining values from list to the GUI
        liczba1 = history[id][2]
        liczba2 = history[id][3]
        temp_type = history[id][0]
        is_inserted = history[id][1]
        self.wpis.setText(liczba1)
        self.wyliczone.setText(history[id][4])
        
    # DEFINING CLEAR FUNCTION, WHICH CLEARS ALL VALUES FROM GUI
    def clear(self):
        
        # Importing global variables
        global temp_type, is_inserted, liczba1, liczba2
        
        # Clearing all the values
        temp_type = ""
        is_inserted = False
        liczba1 = ""
        liczba2 = ""
        
        # Checking, if mode is test or not
        # - This used to insure, that app is posibble to test without GUI
        try:
            self.wyliczone.setText("")
            self.wpis.setText("0")
            return("cleared")
        except AttributeError:
            return("cleared")
    
    # DEFINING CLEAR FUNCTION, WHICH CLEARS ALL VALUES FROM GUI
    def clear_all(self):
        
        # Importing global variables
        global temp_type, is_inserted, liczba1, liczba2, history, id_counter
        
        # Clearing all the values
        temp_type = ""
        is_inserted = False
        liczba1 = ""
        liczba2 = ""
        
        # Checking, if mode is test or not
        # - This used to insure, that app is posibble to test without GUI
        try:
            self.wyliczone.setText("")
            self.wpis.setText("0")
            return("all cleared")
        except AttributeError:
            return("all cleared")
        
    # DEFINING ENTER FUNCTION, WHICH WOULD ENTER VALUES INTO USER INPUT BOX
    def enter(self, letter):
        
        # Importing global variables
        global is_inserted
        
        # Checking, if mode is test or not
        # - This used to insure, that app is posibble to test without GUI
        try:
            
            # Checks, if the value of user input is 0 or Syntax Error. If so, replaces the whole value of input with entered number
            if (self.wpis.text() == "0" or self.wpis.text() == "Syntax Error" or is_inserted == True):
                self.wpis.setText(letter)
                is_inserted = False
                
            # Adds number to the user input
            else:
                self.wpis.setText(self.wpis.text()+letter)
        except AttributeError:
            return(letter)
        
    # DEFINING DELETE FUNCTION, WHICH DELETES LAST ENTERED NUMBER FROM USER INPUT
    def delete(self):
        
        # Checking, if mode is test or not
        # - This used to insure, that app is posibble to test without GUI
        try:
            text = self.wpis.text()
            
            # Checks, if user inputs value is equal to 0 or not
            if (self.wpis != "0"):
                self.wpis.setText(text[:-1])
            if (self.wpis.text() == ""):
                self.wpis.setText("0")
            else:
                pass
        except AttributeError:
            return("deleted")
    
    # DEFINING OPERATION FUNCTION, WHICH BASED ON THE OPERATION SYBOL, MAKES ACTION
    def operation(self, type):
        
        # Importing global variables
        global temp_type, is_inserted, liczba1, liczba2
        
        # Checking, which type of operation is gonna be done
        match type:
            case "power":
                self.wyliczone.setText(self.wpis.text()+"²")
                self.wpis.setText(str(math.pow((float(self.wpis.text())), 2)))
            case "root":
                try:
                    self.wyliczone.setText("√"+self.wpis.text())
                    self.wpis.setText(str(math.sqrt(eval(self.wpis.text()))))
                except:
                    self.wyliczone.setText("√"+self.wpis.text())
                    self.wpis.setText("Syntax Error")
            case "1/X":
                self.wyliczone.setText("1 / "+self.wpis.text()+" =")
                self.wpis.setText(str(1/(eval(self.wpis.text()))))
            case "%":
                self.wyliczone.setText(str(eval(self.wpis.text())/100))
                self.wpis.setText(str((eval(self.wpis.text())/100)))
            case "reverse":
                self.wyliczone.setText(str(eval(self.wpis.text())*-1))
                self.wpis.setText(str(eval(self.wpis.text())*-1))
            case "=":
                liczba2 = self.wpis.text()
                self.oblicz(liczba1=liczba1, liczba2=liczba2, operation=temp_type)
            case _:
                liczba1 = self.wpis.text()
                if (temp_type == type):
                    liczba1 = self.oblicz(liczba1=liczba1, liczba2=liczba2 ,operation=type)
                if (temp_type != type):
                    self.wyliczone.setText(self.wpis.text()+type)
                    liczba2 = self.wpis.text()
                    is_inserted = True
                    temp_type = type
                if (temp_type == ""):
                    self.wyliczone.setText(self.wpis.text())
                    is_inserted = True
    
    # DEFINING OBLICZ FUNCTION, WHICH CALCULATES THE FINAL VALUE OF AN OPERATION
    def oblicz(self, liczba1, liczba2, operation):
        rownanie = liczba1 + str(operation) + liczba2
        try:
            self.wyliczone.setText(rownanie+"=")
        except AttributeError:
            pass
        try:
            try:
                result = str(eval(rownanie))
            except SyntaxError:
                result = "Syntax Error"
            
            self.add_history_item(rownanie=rownanie+"=", result=result)
            try:
                self.wpis.setText(str(result))
            except AttributeError:
                pass
            return(str(result))
        except ZeroDivisionError or ValueError:
            try:
                self.wpis.setText("Syntax Error")
                return("Syntax Error")
            except:
                pass    
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())