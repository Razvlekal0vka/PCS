import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QLabel


def exit():
    sys.exit(app.exec())


class Example(QWidget):
    def __init__(self):
        self.permission = ''
        self.permission_1 = ''
        self.permissions = ['800*450', '1280*720', '1600*900', '1920*1080', '2048*1152', '3840*2160']
        self.new_settings = ['True', '1600*900', '1920*1080']
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 225)
        self.setWindowTitle('PCS')

        self.label_1 = QLabel(self)
        self.label_1.setText("Выберите разрешение вашего экрана и приложения")
        self.label_1.move(15, 15)

        self.label_2 = QLabel(self)
        self.label_2.setText("Разрешение вашего экрана:")
        self.label_2.move(15, 40)

        self.label_3 = QLabel(self)
        self.label_3.setText("Разрешение приложения:")
        self.label_3.move(215, 40)

        self.label_Error = QLabel(self)
        self.label_Error.setText("Error")
        self.label_Error.move(330, 175)
        self.label_Error.hide()

        self.btn = QPushButton('Применить', self)
        self.btn.move(305, 190)
        self.btn.clicked.connect(self.run)

        self.radiobutton_1_1 = QRadioButton('800*450', self)
        self.radiobutton_1_1.move(15, 65)
        self.radiobutton_1_1.toggled.connect(self.dimensions_0)

        self.radiobutton_1_2 = QRadioButton('1280*720', self)
        self.radiobutton_1_2.move(15, 90)
        self.radiobutton_1_2.toggled.connect(self.dimensions_1)

        self.radiobutton_1_3 = QRadioButton('1600*900', self)
        self.radiobutton_1_3.move(15, 115)
        self.radiobutton_1_3.toggled.connect(self.dimensions_2)

        self.radiobutton_1_4 = QRadioButton('1920*1080', self)
        self.radiobutton_1_4.move(15, 140)
        self.radiobutton_1_4.toggled.connect(self.dimensions_3)

        self.radiobutton_1_5 = QRadioButton('2048*1152', self)
        self.radiobutton_1_5.move(15, 165)
        self.radiobutton_1_5.toggled.connect(self.dimensions_4)

        self.radiobutton_1_6 = QRadioButton('3840*2160', self)
        self.radiobutton_1_6.move(15, 190)
        self.radiobutton_1_6.toggled.connect(self.dimensions_5)

        rb_gr = QButtonGroup(self)
        rb_gr.addButton(self.radiobutton_1_1)
        rb_gr.addButton(self.radiobutton_1_2)
        rb_gr.addButton(self.radiobutton_1_3)
        rb_gr.addButton(self.radiobutton_1_4)
        rb_gr.addButton(self.radiobutton_1_5)
        rb_gr.addButton(self.radiobutton_1_6)

        self.radiobutton_2_1 = QRadioButton('800*450', self)
        self.radiobutton_2_1.move(215, 65)
        self.radiobutton_2_1.toggled.connect(self.dimensions_0_1)

        self.radiobutton_2_2 = QRadioButton('1280*720', self)
        self.radiobutton_2_2.move(215, 90)
        self.radiobutton_2_2.toggled.connect(self.dimensions_1_1)

        self.radiobutton_2_3 = QRadioButton('1600*900', self)
        self.radiobutton_2_3.move(215, 115)
        self.radiobutton_2_3.toggled.connect(self.dimensions_2_1)

        self.radiobutton_2_4 = QRadioButton('1920*1080', self)
        self.radiobutton_2_4.move(215, 140)
        self.radiobutton_2_4.toggled.connect(self.dimensions_3_1)

        self.radiobutton_2_5 = QRadioButton('2048*1152', self)
        self.radiobutton_2_5.move(215, 165)
        self.radiobutton_2_5.toggled.connect(self.dimensions_4_1)

        self.radiobutton_2_6 = QRadioButton('3840*2160', self)
        self.radiobutton_2_6.move(215, 190)
        self.radiobutton_2_6.toggled.connect(self.dimensions_5_1)

        rb_gr1 = QButtonGroup(self)
        rb_gr1.addButton(self.radiobutton_2_1)
        rb_gr1.addButton(self.radiobutton_2_2)
        rb_gr1.addButton(self.radiobutton_2_3)
        rb_gr1.addButton(self.radiobutton_2_4)
        rb_gr1.addButton(self.radiobutton_2_5)
        rb_gr1.addButton(self.radiobutton_2_6)

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

    def dimensions_4(self):
        self.label_Error.hide()
        self.permission = self.permissions[4]

    def dimensions_5(self):
        self.label_Error.hide()
        self.permission = self.permissions[5]

    def dimensions_0_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[0]

    def dimensions_1_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[1]

    def dimensions_2_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[2]

    def dimensions_3_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[3]

    def dimensions_4_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[4]

    def dimensions_5_1(self):
        self.label_Error.hide()
        self.permission_1 = self.permissions[5]

    def run(self):
        permission, permission_1 = self.permission.split('*'), self.permission_1.split('*')
        if self.permission not in self.permissions or self.permission_1 not in self.permissions or int(permission[0]) < int(permission_1[0]) or int(permission[1]) < int(permission_1[1]):
            self.label_Error.show()
        else:
            self.check_and_settings()

    def check_and_settings(self):
        settings = []
        settings.append('True')
        settings.append(self.permission)
        settings.append(self.permission_1)
        settings_file = open('data/settings.txt', 'w')
        for elem_num in range(len(settings)):
            if elem_num == len(settings) - 1:
                settings_file.write(f'''{settings[elem_num]}''')
            else:
                settings_file.write(f'''{settings[elem_num]}\n''')
        settings_file.close()
        os.system('examination.py')
        exit()


code = 'start'
lines = []
if code == 'start':
    try:
        set_list = open('data/settings.txt', 'r')
        num_line = 0
        for line in set_list:
            line = line.replace('\n', '', 1)
            if num_line == 0:
                if line == 'False' or line != 'True':
                    code = 'new_set'
            elif num_line == 1 or num_line == 2:
                lines.append(line)
                if line != '800*450' and line != '1280*720' and line != '1600*900' and line != '1920*1080' and \
                        line != '2048*1152' and line != '3840*2160':
                    code = 'new_set'
                else:
                    if line == '800*450' or line == '1280*720' or line == '1600*900' or line == '1920*1080' or \
                            line == '2048*1152' or line == '3840*2160':
                        pass
                    else:
                        code = 'new_set'
            num_line += 1
        if num_line < 3:
            code = 'new_set'
        else:
            l1, l2 = lines[0].split('*'), lines[1].split('*')
            if int(l1[0]) < int(l2[0]) or int(l1[1]) < int(l2[1]):
                code = 'new_set'
        set_list.close()
    except Exception as e:
        code = 'new_set'
    if code == 'start':
        os.system('examination.py')
        sys.exit()

if code == 'new_set':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
