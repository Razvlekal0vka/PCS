import os
import socket
from tkinter import filedialog, Tk, Button, ttk
from tkinter import messagebox as mb

ip = '26.137.155.119'
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
        print('Ошибка связанная с функцией /send_file\\', exception)


def send_files_with_open_file_dialog_window(address):
    # Прячем главное окно tkinter
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    root.destroy()

    try:
        for file in files:
            send_file(file, address)
            print(file, 'received')

    except Exception as exception:
        print(f'Ошибка связанная с функцией /send_files_with_open_file_dialog_window\\', exception)


def get_answer():
    root = Tk()
    root.withdraw()
    answer = mb.askyesno(title="Вопрос", message="Вы хотите продолжить выполнение программы?")
    root.destroy()
    return answer


start = True
while start:
    def send_to_server():
        send_files_with_open_file_dialog_window(address)


    def get_from_server():
        pass


    def stop():
        global start
        start = False
        tkWindow.destroy()

    if start:
        tkWindow = Tk()
        tkWindow.geometry('200x100')
        tkWindow.title('Window')
        style = ttk.Style(tkWindow)
        style.theme_use("clam")
        Button(tkWindow, text='Скачать с сервера', command=get_from_server, background='black', foreground='white').pack()
        Button(tkWindow, text='Загрузить на сервер', command=send_to_server, background='black', foreground='white').pack()
        Button(tkWindow, text='Остановить программу', command=stop, background='black', foreground='white').pack()
        tkWindow['bg'] = 'black'
        ttk.Style().configure(Button, )

        tkWindow.mainloop()
