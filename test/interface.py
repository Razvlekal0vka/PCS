import os
import socket
import tkinter as tk
from time import sleep
from tkinter import Button, filedialog, Menu


def send():
    files = filedialog.askopenfilenames()
    addr = "26.199.217.122"
    port = 0
    try:
        sock = socket.socket()
        sock.connect((addr, 9999))
        print(os.getlogin())
        send = bytes(os.getlogin(), 'utf8')
        sock.send(send)
        portN = (sock.recv(1024)).decode('UTF-8')
        print(portN)
        sock.close()
        del sock
        for i in files:
            sleep(0.2)
            sock = socket.socket()
            sock.connect((addr, int(portN)))
            sock.send(bytes(i, 'utf8'))
            f = open(i, "rb")
            # читаем строку
            l = f.read(1024)
            while (l):
                # отправляем строку на сервер
                sock.send(l)
                l = f.read(1024)
            f.close()
            sock.close()
    except Exception as exc:
        print(exc)
        error = 'ошибка номер ....'
        print("ошибка с текстом, строка, линия и т.п. тип ошибки(что пишет компилятор): " + str(error))


window = tk.Tk()
window.geometry('800x480')
# lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
btn = Button(window, text="Send", command=send)
btn.grid(column=1, row=0)
# files = filedialog.askopenfilenames()
# print(files)


menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()
