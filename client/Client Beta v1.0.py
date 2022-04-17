import socket
from tkinter import filedialog, Tk

ip = '26.43.19.188'
port = 53210

address = ip, port


def send_file(file, address):
    try:
        # создаём сокет для подключения
        sock = socket.socket()
        sock.connect(address)

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

    except Exception as exception:
        print('Связанная ошибка с функцией /send_file\\', exception)


def send_files_with_open_file_dialog_window(address):

    # Прячем главное окно tkinter
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    root.destroy()

    try:
        for file in files:
            send_file(file, address)

    except Exception as exception:
        print('Связанная ошибка с функцией /send_files_with_open_file_dialog_window\\', exception)


send_files_with_open_file_dialog_window(address)
