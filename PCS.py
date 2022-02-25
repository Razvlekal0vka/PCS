import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        self.read_data, self.screen_resolution = [], []
        super().__init__()
        self.initUI()

    def read(self):
        set_list = open('data/settings.txt', 'r')
        num_line = 0
        for line in set_list:
            line = line.replace('\n', '', 1)

            if num_line == 1:
                if line == '800*600' or line == '1024*768' or line == '1280*1024' or line == '1600*800':
                    self.screen_resolution = line.split('*')
                    print(self.screen_resolution)

            self.read_data.append(line)
            num_line += 1

    def initUI(self):
        self.read()

        self.setGeometry(100, 100, int(self.screen_resolution[0]), int(self.screen_resolution[1]))
        self.setWindowTitle('PCS')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
