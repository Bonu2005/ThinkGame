from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont

# Set font globally
font = QFont("Arial", 18)

app = QApplication([])

class Window(QWidget):
    def __init__(self, title, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, width, height)
        self.tugmachalar()  # Call the method to add the main buttons

    def bir_chi(self):
        # Creating buttons when 1-chi is pressed
        btn = QPushButton( self)
        btn1 = QPushButton( self)
        btn2 = QPushButton( self)
        btn3 = QPushButton( self)

        # Set button geometry (x, y, width, height)
        btn.setGeometry(10, 70, 50, 50)
        btn.setStyleSheet("background-color:#6d40bba8;border-radius:8px ")
        btn1.setGeometry(10, 120, 50, 50)
        btn1.setStyleSheet("background-color:#6d40bba8;border-radius:8px")
        btn2.setGeometry(10, 170, 50, 50)
        btn2.setStyleSheet("background-color:#6d40bba8;border-radius:8px")
        btn3.setGeometry(60, 70, 50, 50)
        btn3.setStyleSheet("background-color:#6d40bba8;border-radius:8px")
        btn.show()
        btn1.show()
        btn2.show()
        btn3.show()

    def ikki_chi(self):
        # Creating buttons when 1-chi is pressed
        btn = QPushButton( self)
        btn1 = QPushButton( self)
        btn2 = QPushButton( self)
        btn3 = QPushButton( self)

        # Set button geometry (x, y, width, height)
        btn.setGeometry(110, 120, 50, 50)
        btn.setStyleSheet("background-color:#b550e8a8e;border-radius:8px ")
        btn1.setGeometry(160, 120, 50, 50)
        btn1.setStyleSheet("background-color:#b550e8a8e;border-radius:8px")
        btn2.setGeometry(110, 170, 50, 50)
        btn2.setStyleSheet("background-color:#b550e8a8e;border-radius:8px")
        btn3.setGeometry(160, 170, 50, 50)
        btn3.setStyleSheet("background-color:#b550e8a8e;border-radius:8px")
        btn.show()
        btn1.show()
        btn2.show()
        btn3.show()


    def uch_chi(self):
        btn = QPushButton( self)
        btn1 = QPushButton( self)
        btn2 = QPushButton( self)
        btn3 = QPushButton( self)

        # Set button geometry (x, y, width, height)
        btn.setGeometry(230, 170, 50, 50)
        btn.setStyleSheet("background-color: #4200b3;border-radius:8px ")
        btn1.setGeometry(280, 170, 50, 50)
        btn1.setStyleSheet("background-color: #4200b3;border-radius:8px")
        btn2.setGeometry(330, 170, 50, 50)
        btn2.setStyleSheet("background-color: #4200b3;border-radius:8px")
        btn3.setGeometry(380, 170, 50, 50)
        btn3.setStyleSheet("background-color: #4200b3;border-radius:8px")
        btn.show()
        btn1.show()
        btn2.show()
        btn3.show()

    def tort_chi(self):
        btn = QPushButton( self)
        btn1 = QPushButton( self)
        btn2 = QPushButton( self)
        btn3 = QPushButton( self)

        # Set button geometry (x, y, width, height)
        btn.setGeometry(470, 170, 50, 50)
        btn.setStyleSheet("background-color: rgb(73, 4, 7);border-radius:8px ")
        btn1.setGeometry(470, 120, 50, 50)
        btn1.setStyleSheet("background-color: rgb(73, 4, 7);border-radius:8px")
        btn2.setGeometry(520, 120, 50, 50)
        btn2.setStyleSheet("background-color: rgb(73, 4, 7);border-radius:8px")
        btn3.setGeometry(520, 70, 50, 50)
        btn3.setStyleSheet("background-color:  rgb(73, 4, 7);border-radius:8px")
        btn.show()
        btn1.show()
        btn2.show()
        btn3.show()

    def tugmachalar(self):
        # Main buttons
        btn = QPushButton("1-chi", self)
        btn1 = QPushButton("2-chi", self)
        btn2 = QPushButton("3-chi", self)
        btn3 = QPushButton("4-chi", self)

        # Set button geometry (x, y, width, height)
        btn.setGeometry(40, 20, 50, 50)
        btn.clicked.connect(self.bir_chi)  # Connect 1-chi button to bir_chi method
        btn1.setGeometry(140, 20, 50, 50)
        btn1.clicked.connect(self.ikki_chi)
        btn2.setGeometry(300, 20, 50, 50)
        btn2.clicked.connect(self.uch_chi)
        btn3.setGeometry(480, 20, 50, 50)
        btn3.clicked.connect(self.tort_chi)

win = Window("OOP", 800, 600)
win.show()

app.exec_()