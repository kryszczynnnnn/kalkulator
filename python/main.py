from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(QSize(320, 560))
        
        self.layout = QHBoxLayout()
        main = QWidget()
        self.wpis = QLabel()
        
        row1 = QVBoxLayout()
        row2 = QVBoxLayout()
        row3 = QVBoxLayout()
        row4 = QVBoxLayout()
        
        for i in range(1, 4):
            guzik = QPushButton(text=str(i))
            guzik.clicked.connect(lambda:print(i))
            row1.addWidget(guzik)
        
        self.layout.addLayout(row1)
        main.setLayout(self.layout)
        self.setCentralWidget(main)
                
        
        
        
    def wpisz(self, wpis):
        print(wpis)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())