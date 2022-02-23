import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel


def next():
    os.system('PCS.py')
    sys.exit()


class Example(QWidget):
    def __init__(self):
        self.permission = ''
        self.permissions = ['800*600', '1024*768', '1280*1024', '1600*800']
        self.new_settings = ['True',
                             '1600*800']
        super().__init__()
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
        else:
            self.check_and_settings()

    def check_and_settings(self):
        settings = []
        settings.append('True')
        settings.append(self.permission)
        settings_file = open('data/settings.txt', 'w')
        for line in settings:
            if line == settings[-1]:
                settings_file.write(f'''{line}''')
            else:
                settings_file.write(f'''{line}\n''')
        settings_file.close()
        next()


code = 'start'
if code == 'start':
    try:
        set_list = open('data/settings.txt', 'r')
        num_line = 0
        for line in set_list:
            line = line.replace('\n', '', 1)
            if num_line == 0:
                if line == 'False' or line != 'True':
                    code = 'new_set'
            if num_line == 1:
                if line != '800*600' and line != '1024*768' and line != '1280*1024' and line != '1600*800':
                    code = 'new_set'
                else:
                    if line == '800*600' or line == '1024*768' or line == '1280*1024' or line == '1600*800':
                        pass
                    else:
                        code = 'new_set'
            num_line += 1
        if num_line < 2:
            code = 'new_set'
        set_list.close()
    except Exception as e:
        code = 'new_set'
    if code == 'start':
        next()

if code == 'new_set':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
