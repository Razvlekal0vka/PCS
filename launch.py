import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        self.permission = -1
        self.permission_1, self.permission_2 = '', ''
        self.permissions = ['800*600', '1024*768', '1280*1024', '1600*800']
        self.permission_modes = [0, 1, 2, 3, 4]
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 235, 165)
        self.setWindowTitle('PCS')

        self.label = QLabel(self)
        self.label.setText("Доступные разрешения:")
        self.label.move(10, 15)

        self.label_Error = QLabel(self)
        self.label_Error.setText("Error")
        self.label_Error.move(175, 115)
        self.label_Error.hide()

        self.btn = QPushButton('Применить', self)
        self.btn.move(150, 135)
        self.btn.clicked.connect(self.run)

        self.fir_input = QLineEdit(self)
        self.fir_input.move(30, 135)
        self.fir_input.resize(35, 20)

        self.label = QLabel(self)
        self.label.setText("*")
        self.label.move(65, 140)

        self.sec_input = QLineEdit(self)
        self.sec_input.move(71, 135)
        self.sec_input.resize(35, 20)

        self.radiobutton = QRadioButton('800*600', self)
        self.radiobutton.move(10, 40)
        self.radiobutton.country = 0
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton('1024*768', self)
        self.radiobutton.move(10, 65)
        self.radiobutton.country = 1
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton('1280*1024', self)
        self.radiobutton.move(10, 90)
        self.radiobutton.country = 2
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton('1600*800', self)
        self.radiobutton.move(10, 115)
        self.radiobutton.country = 3
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton('', self)
        self.radiobutton.move(10, 140)
        self.radiobutton.country = 4
        self.radiobutton.toggled.connect(self.onClicked)

    def onClicked(self):
        radioButton = self.sender()
        self.label_Error.hide()
        if radioButton.isChecked():
            self.permission = radioButton

    def run(self):
        x, y = list(map(int, [self.fir_input.text(), self.sec_input.text()]))
        self.permission_1, self.permission_2 = x, y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
