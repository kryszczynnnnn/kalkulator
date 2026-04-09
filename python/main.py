from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QGridLayout, QGroupBox, QDialog
from PyQt5.QtGui import QIcon
import math
from style import QSS
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(QSize(320, 400))
        self.setStyleSheet(QSS)
        self.initUI()
        
    def initUI(self):
        self.createGridLayout()
        
        self.wyliczone = QLabel("", objectName="wyliczone")
        self.wpis = QLabel("0", objectName="wpis")
        
        self.wpis.setAlignment(Qt.AlignRight)
        self.wyliczone.setAlignment(Qt.AlignRight)
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.wyliczone)
        windowLayout.addWidget(self.wpis)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
        
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 4)
        
        # ROW 1
        percent_button = QPushButton(text="%")
        percent_button.clicked.connect(lambda:self.operation(type="%"))
        layout.addWidget(percent_button, 0, 0)
        
        clear_all_button = QPushButton(text="CE")
        clear_all_button.clicked.connect(lambda:self.clear_all)
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
        equals_button.clicked.connect(lambda:self.operation(type="="))
        layout.addWidget(equals_button, 6, 3)
        
        self.horizontalGroupBox.setLayout(layout)
        
    def clear(self):
        self.wyliczone.setText("")
        self.wpis.setText("0")
        
    def clear_all(self):
        self.wyliczone.setText("")
        self.wpis.setText("0")
        
    def enter(self, letter):
        if (self.wpis.text() == "0"):
            self.wpis.setText(letter)
        else:
            self.wpis.setText(self.wpis.text()+letter)
        
    def delete(self):
        text = self.wpis.text()
        if (self.wpis != "0"):
            self.wpis.setText(text[:-1])
        if (self.wpis.text() == ""):
            self.wpis.setText("0")
        else:
            pass
        
    def operation(self, type):
        match type:
            case "/":
                self.wyliczone.setText(self.wpis.text()+"/")
                self.wpis.setText("")
            case "*":
                self.wyliczone.setText(self.wpis.text()+"*")
                self.wpis.setText("")
            case "-":
                self.wyliczone.setText(self.wpis.text()+"-")
                self.wpis.setText("")
            case "+":
                self.wyliczone.setText(self.wpis.text()+"+")
                self.wpis.setText("")
            case "=":
                rownanie = self.wyliczone.text() + self.wpis.text()
                self.wyliczone.setText(rownanie+"=")
                result = eval(rownanie)
                self.wpis.setText(str(result))
                again = again + 1
            case "power":
                self.wyliczone.setText(self.wpis.text()+"²")
                self.wpis.setText(str((eval(self.wpis.text()))^2))
            case "root":
                self.wyliczone.setText("√"+self.wpis.text())
                self.wpis.setText(str(math.sqrt(eval(self.wpis.text()))))
            case "1/X":
                self.wyliczone.setText("1 / "+self.wpis.text()+" =")
                self.wpis.setText(str(1/(eval(self.wpis.text()))))
            case "%":
                self.wyliczone.setText(str(eval(self.wpis.text())/100))
                self.wpis.setText(str((eval(self.wpis.text())/100)))
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())