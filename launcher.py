import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel


def check_settings(start_settings):
    settings = []
    try:
        set_list = open('data/settings.txt', 'r')
        num_line = 0
        for line in set_list:
            line = line.replace("\n", "")

            if num_line == 0:
                if start_settings[0] in line:
                    if start_settings[0] == line:
                        settings.append(f'''{line}\n''')
                    else:
                        words = line.split()
                        if words[2] == 'True' or words[2] == 'False':
                            settings.append(f'''{line}\n''')
                        else:
                            settings.append(f'''{start_settings[0]}\n''')
                else:
                    settings.append(f'''{start_settings[0]}\n''')
                num_line += 1

            elif num_line == 1:
                if line == '':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[1]}\n''')
                num_line += 1

            elif num_line == 2:
                if line == 'window dimensions:':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[2]}\n''')
                num_line += 1

            elif num_line == 3:
                if line == '1 - 800*600':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[3]}\n''')
                num_line += 1

            elif num_line == 4:
                if line == '2 - 1024*768':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[4]}\n''')
                num_line += 1

            elif num_line == 5:
                if line == '3 - 1280*1024':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[5]}\n''')
                num_line += 1

            elif num_line == 6:
                if line == '4 - 1600*800':
                    settings.append(f'''{line}\n''')
                else:
                    settings.append(f'''{start_settings[6]}\n''')
                num_line += 1

            elif num_line == 7:
                if start_settings[7] in line:
                    if start_settings[7] == line:
                        settings.append(f'''{line}\n''')
                    else:
                        words = line.split()
                        if words[2] == '800*600' or words[2] == '1024*768' or words[2] == '1280*1024' or \
                                words[2] == '1600*800':
                            settings.append(f'''{line}\n''')
                        else:
                            settings.append(f'''{start_settings[7]}\n''')
                else:
                    settings.append(f'''{start_settings[7]}\n''')
                num_line += 1

        set_list.close()
        recording_settings(settings)

    except Exception as e:
        raise recording_settings(start_settings)


def recording_settings(settings):
    settings_file = open('data/settings.txt', 'w')
    for line in settings:
        settings_file.write(line)


class Example(QWidget):
    def __init__(self):
        self.permission = ''
        self.permissions = ['800*600', '1024*768', '1280*1024', '1600*800']
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


new_settings = ['first start - False',
                '',
                'window dimensions:',
                '1 - 800*600',
                '2 - 1024*768',
                '3 - 1280*1024',
                '4 - 1600*800',
                'used -',
                '']

check_settings(new_settings)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
