from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QGridLayout, QGroupBox, QDialog
from PyQt5.QtGui import QIcon
import math
from style import QSS
import sys

temp_type = ""
is_inserted = False
liczba1 = ""
liczba2 = ""
history = []
id_counter = 0

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(QSize(400, 400))
        self.setStyleSheet(QSS)
        self.initUI()
        
    def initUI(self):
        self.calculator()
        
        self.wyliczone = QLabel("", objectName="wyliczone")
        self.wpis = QLabel("0", objectName="wpis")
        
        self.wpis.setAlignment(Qt.AlignRight)
        self.wyliczone.setAlignment(Qt.AlignRight)
        self.history_widget = QVBoxLayout()
        
        windowLayout = QHBoxLayout()
        calculator_layout = QVBoxLayout()
        calculator_layout.addWidget(self.wyliczone)
        calculator_layout.addWidget(self.wpis)
        calculator_layout.addWidget(self.horizontalGroupBox)
        windowLayout.addLayout(calculator_layout)
        windowLayout.addLayout(self.history_widget)
        self.setLayout(windowLayout)
        
        self.show()    
    
    def calculator(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 4)
        
        # ROW 1
        percent_button = QPushButton(text="%")
        percent_button.clicked.connect(lambda:self.operation(type="%"))
        layout.addWidget(percent_button, 0, 0)
        
        clear_all_button = QPushButton(text="CE")
        clear_all_button.clicked.connect(self.clear_all)
        layout.addWidget(clear_all_button, 0, 1)
        
        clear_button = QPushButton(text="C")
        clear_button.clicked.connect(self.clear)
        layout.addWidget(clear_button, 0, 2)
        
        delete_button = QPushButton(text="<-")
        delete_button.clicked.connect(self.delete)
        layout.addWidget(delete_button, 0, 3)
        
        # ROW 2
        ulamek_button = QPushButton(text="1/X")
        ulamek_button.clicked.connect(lambda:self.operation(type="1/X"))
        layout.addWidget(ulamek_button, 1, 0)
        
        square_root_button = QPushButton(text="√X")
        square_root_button.clicked.connect(lambda:self.operation(type="root"))
        layout.addWidget(square_root_button, 1, 1)
        
        power_button = QPushButton(text="X²")
        power_button.clicked.connect(lambda:self.operation(type="power"))
        layout.addWidget(power_button, 1, 2)
        
        operation_symbols=["/", "*", "+", "-"]
        
        for i in range(1, len(operation_symbols)+1):
            symbol = operation_symbols[i-1]
            button = QPushButton(text=symbol)
            button.clicked.connect(lambda _, t=button.text(): self.operation(type=t))
            layout.addWidget(button, i, 3)
        
        # NUMPAD
        for i in range(2,5):
            for j in range(0, 3):
                button = QPushButton(text=str(j+(i-2)*3+1))
                button.clicked.connect(lambda _, t=button.text(): self.enter(letter=t))
                layout.addWidget(button, i, j)
                
        # ROW 6
        reverse_button = QPushButton(text="+/-")
        reverse_button.clicked.connect(lambda:self.operation(type="reverse"))
        layout.addWidget(reverse_button, 6, 0)
        
        zero_button = QPushButton(text="0")
        zero_button.clicked.connect(lambda:self.enter(zero_button.text()))
        layout.addWidget(zero_button, 6, 1)
        
        dot_button = QPushButton(text=".")
        dot_button.clicked.connect(lambda:self.enter(dot_button.text()))
        layout.addWidget(dot_button, 6, 2)
        
        equals_button = QPushButton(text="=")
        equals_button.clicked.connect(lambda:self.operation(type=equals_button.text()))
        layout.addWidget(equals_button, 6, 3)
        
        self.horizontalGroupBox.setLayout(layout)
        
    def add_history_item(self, rownanie, result):
        global temp_type, is_inserted, liczba1, liczba2, id_counter
        id = id_counter
        history_button = QPushButton(text = rownanie+result)
        history_button.clicked.connect(lambda _, t=history_button.text(): self.history_item_action(id))
        self.history_widget.addWidget(history_button)
        history.append([temp_type, is_inserted, liczba1, liczba2, rownanie])
        id_counter = id_counter + 1
        
    def history_item_action(self, id):
        global temp_type, is_inserted, liczba1, liczba2, history
        liczba1 = history[id][2]
        liczba2 = history[id][3]
        temp_type = history[id][0]
        is_inserted = history[id][1]
        self.wpis.setText(liczba1)
        self.wyliczone.setText(history[id][4])
        
    def clear(self):
        global temp_type, is_inserted, liczba1, liczba2
        temp_type = ""
        is_inserted = False
        liczba1 = ""
        liczba2 = ""
        try:
            self.wyliczone.setText("")
            self.wpis.setText("0")
            return("cleared")
        except AttributeError:
            return("cleared")
        
    def clear_all(self):
        global temp_type, is_inserted, liczba1, liczba2
        try:
            self.wyliczone.setText("")
            self.wpis.setText("0")
            return("all cleared")
        except AttributeError:
            return("all cleared")
        
    def enter(self, letter):
        try:
            if (self.wpis.text() == "0" or self.wpis.text() == "Syntax Error" or is_inserted == True):
                self.wpis.setText(letter)
            else:
                self.wpis.setText(self.wpis.text()+letter)
        except AttributeError:
            return(letter)
        
    def delete(self):
        try:
            text = self.wpis.text()
            if (self.wpis != "0"):
                self.wpis.setText(text[:-1])
            if (self.wpis.text() == ""):
                self.wpis.setText("0")
            else:
                pass
        except AttributeError:
            return("deleted")
        
    def operation(self, type):
        global temp_type, is_inserted, liczba1, liczba2
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
    
    def oblicz(self, liczba1, liczba2, operation):
        rownanie = liczba1 + str(operation) + liczba2
        try:
            self.wyliczone.setText(rownanie+"=")
        except AttributeError:
            pass
        try:
            result = str(eval(rownanie))
            self.add_history_item(rownanie=rownanie+"=", result=result)
            return(str(result))
        except ZeroDivisionError or ValueError:
            try:
                self.wpis.setText("Syntax Error")
                return("Syntax Error")
            except:
                pass    
        try:
            self.wpis.setText(str(result))
        except AttributeError:
            pass
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())