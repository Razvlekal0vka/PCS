import socket
from tkinter import filedialog

ip = '26.43.19.188'
port = 53210


def send_files_with_file_dialog_window(ip, port):
    files = filedialog.askopenfilenames()

    for file in files:
        # создаём сокет для подключения
        sock = socket.socket()
        sock.connect((ip, port))

        # запрашиваем имя файла и отправляем серверу
        sock.send((bytes(file, encoding='UTF-8')))

        # открываем файл в режиме байтового чтения
        f = open(file, "rb")

        # читаем строку
        bite_line = f.read(1024)

        while bite_line:
            # отправляем строку на сервер
            sock.send(bite_line)
            bite_line = f.read(1024)

        f.close()
        sock.close()


send_files_with_file_dialog_window(ip, port)

