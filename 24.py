from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import sys
import random

fon = QFont("Papyrus", 22)
fon1 = QFont("Papyrus", 18)
app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Полноэкранное окно")
        self.setStyleSheet("background-color:black;")
        self.main()

    def main(self):
        self.lab = QLabel(self)
        self.lab.setText("Yangi o'yin-yangi imkoniyatlar.\nQobilyatingizni ko'rsatishga tayyormisiz?")
        self.lab.setFont(fon)
        self.lab.setStyleSheet("color:purple")
        self.lab.setAlignment(QtCore.Qt.AlignCenter)
        self.lab.setGeometry(100, 200, self.width(), self.height())

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("./img/image.png"))
        self.image_label.setScaledContents(True)
        self.image_width = 100
        self.image_height = 100
        self.image_label.setGeometry(1000, 300, self.width(), self.height())

        self.btn = QPushButton(self)
        self.btn.setText("O'yinni Boshlash uchun bos!")
        self.btn.setGeometry(300, 600, 400, 100)
        self.btn.setStyleSheet("background-color:orange;color:purple")
        self.btn.setFont(fon1)
        self.btn.clicked.connect(self.open_window)
        self.btn.show()
        
        self.Second_Window = Window1()

    def open_window(self):
        self.Second_Window.showFullScreen()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.close()

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(1, 63, 48);")
        self.setWindowTitle("Полноэкранное окно")
        self.setGeometry(800, 600, 500, 400)
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 4 
        self.result_label = QLabel("  1 dan  100 gacha", self)
        self.result_label.setStyleSheet("color:yellow;")
        self.result_label.setFont(fon)
        self.result_label.setGeometry(200,500,900,600)
        self.lab=QLabel(self)
        self.lab.setText("Biz bir son oyladik...\n Oyinni maqsadi shuki shu sinni topishingiz kerak")
        self.lab.setStyleSheet("color:yellow")
        self.lab.setFont(fon)
        self.lab.setGeometry(200,0,800,600)
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(200,500,200,100)
        self.line_edit.setFont(fon1)
        self.line_edit.setStyleSheet("QLineEdit {"
                             "border-radius: 20px;"  
                             "background-color: yellow;" 
                             "}")
        self.button = QPushButton("Urinish", self)
        self.button.setStyleSheet("QPushButton {"
                             "border-radius: 20px;"  
                             "background-color: yellow;" 
                             "}")
        self.button.setFont(fon1)
        self.button.setGeometry(700,500,200,100)

        self.button.clicked.connect(self.check_guess)
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("./img/image copy.png"))
        self.image_label.setScaledContents(True)
        self.image_width = 1000
        self.image_height = 1000
        self.image_label.setGeometry(1100, 350, self.width(), self.height())

        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.close()

    def check_guess(self):
        guess_text = self.line_edit.text()
        try:
            guess = int(guess_text)
            if self.attempts_left > 0:
                if guess < self.secret_number:
                    self.result_label.setText(f"oylangan son  kattaroq! Urinishlar soni: {self.attempts_left}")
                elif guess > self.secret_number:
                    self.result_label.setText(f"oylangan son kichikriq! Urinishlar soni: {self.attempts_left}")
                else:
                    self.result_label.setText("Tabriklamiz! Topdingiz! 🥳")
                    
                    self.secret_number = random.randint(1, 100)
                    self.attempts_left = 4  
                    return
                self.attempts_left -= 1
            else:
                self.result_label.setText(f"Afsus bu safar omadingiz kelmadi ☹️! Oylangan son {self.secret_number}")
        except ValueError:
            self.result_label.setText("Iltimos, son kiriting!")

win = Window()
win.showFullScreen()

app.exec_()



from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton("Кнопка", self)
        button.setGeometry(50, 50, 200, 50)

        
        button.setStyleSheet("QPushButton {"
                             "border-radius: 20px;" 
                             "background-color: lightblue;" 
                             "}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())