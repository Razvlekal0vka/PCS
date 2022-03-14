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

            if num_line == 2:
                if line == '800*450' or line == '1280*720' or line == '1600*900' or line == '1920*1080' or \
                            line == '2048*1152' or line == '3840*2160':
                    self.screen_resolution = line.split('*')
                    print(self.screen_resolution)

            self.read_data.append(line)
            num_line += 1

    def initUI(self):
        self.read()
        print(int(self.screen_resolution[0]), int(self.screen_resolution[1]))
        self.setGeometry(100, 100, int(self.screen_resolution[0]), int(self.screen_resolution[1]))
        self.setWindowTitle('Personal Cloud Sync')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
