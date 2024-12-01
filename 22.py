import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QComboBox, QVBoxLayout, QLineEdit, QLabel, QPushButton
)
from PyQt5 import QtCore

response = requests.get('https://nbu.uz/uz/exchange-rates/json')
valyutalar = response.json()

nomlari = [valyuta["title"] for valyuta in valyutalar]

narxlari = {valyuta["title"]: float(valyuta["cb_price"]) for valyuta in valyutalar}


class Window(QWidget):
    def __init__(self, title, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.menu = QComboBox(self)
        self.menu.addItems(nomlari)
        self.layout.addWidget(self.menu)

        self.lne = QLineEdit(self)
        self.lne.setPlaceholderText("Miqdor kiriting:")
        self.layout.addWidget(self.lne)

        self.label = QLabel(self)
        
        self.label.setStyleSheet("color:green")
        self.label.setText("Natija: ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setStyleSheet("font-size: 24px; border: 1px solid black; padding: 10px;")
        self.layout.addWidget(self.label)

        self.btn = QPushButton("Almashtirish", self)
        self.layout.addWidget(self.btn)

        self.btn.clicked.connect(self.show_result)

    def show_result(self):
        amount = float(self.lne.text())  # Foydalanuvchi kiritgan miqdorni olish
        selected_currency = self.menu.currentText()  # Foydalanuvchi tanlagan valyutani olish
        conversion_rate = narxlari[selected_currency]  # Tanlangan valyutaning narxini olish
        result = amount * conversion_rate  # Almashtirishni  hisoblash
        self.label.setText(f"Natija: {amount} {selected_currency} = {result:.2f} UZS")  

app = QApplication([])
win = Window("Valyuta Ayirboshlash", 1000, 800) 
win.show()
app.exec_()