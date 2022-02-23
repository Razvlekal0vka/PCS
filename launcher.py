import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel



class Example(QWidget):
    def __init__(self):
        self.permission = ''
        self.permission_1, self.permission_2 = '', ''
        self.permissions = ['800*600', '1024*768', '1280*1024', '1600*800']
        super().__init__()
        self.check_settings()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 235, 145)
        self.setWindowTitle('PCS')

        self.label = QLabel(self)
        self.label.setText("Доступные разрешения:")
        self.label.move(10, 15)

        self.label_Error = QLabel(self)
        self.label_Error.setText("Error")
        self.label_Error.move(175, 95)
        self.label_Error.hide()

        self.btn = QPushButton('Применить', self)
        self.btn.move(150, 115)
        self.btn.clicked.connect(self.run)

        self.radiobutton = QRadioButton('800*600', self)
        self.radiobutton.move(10, 40)
        self.radiobutton.toggled.connect(self.dimensions_0)

        self.radiobutton = QRadioButton('1024*768', self)
        self.radiobutton.move(10, 65)
        self.radiobutton.toggled.connect(self.dimensions_1)

        self.radiobutton = QRadioButton('1280*1024', self)
        self.radiobutton.move(10, 90)
        self.radiobutton.toggled.connect(self.dimensions_2)

        self.radiobutton = QRadioButton('1600*800', self)
        self.radiobutton.move(10, 115)
        self.radiobutton.toggled.connect(self.dimensions_3)

    def dimensions_0(self):
        self.label_Error.hide()
        self.permission = self.permissions[0]

    def dimensions_1(self):
        self.label_Error.hide()
        self.permission = self.permissions[1]

    def dimensions_2(self):
        self.label_Error.hide()
        self.permission = self.permissions[2]

    def dimensions_3(self):
        self.label_Error.hide()
        self.permission = self.permissions[3]

    def run(self):
        if self.permission not in self.permissions:
            self.label_Error.show()
        self.check_settings()

    def check_settings(self):
        settings = ['first start - False', '', 'window dimensions:', '1 - 800*600', '2 - 1024*768', '3 - 1280*1024', '4 - 1600*800', 'used - n', '']
        try:
            set_list = open('settings.txt', 'r')
            num_line = 0
            for line in set_list:
                print(line)
                if num_line == 0:
                    pass
        except Exception as e:
            raise print('ggg')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
