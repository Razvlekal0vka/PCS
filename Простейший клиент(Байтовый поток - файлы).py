import socket

ip = '26.43.19.188'
port = 53210

# создаём сокет для подключения
sock = socket.socket()
sock.connect((ip, port))

# запрашиваем имя файла и отправляем серверу
f_name = input('File to send: ')
sock.send((bytes(rf'{f_name}', encoding='UTF-8')))

# открываем файл в режиме байтового чтения
f = open(rf'{f_name}'.replace('\\', '/'), "rb")

# читаем строку
bite_line = f.read(1024)

while bite_line:
    # отправляем строку на сервер
    sock.send(bite_line)
    bite_line = f.read(1024)

f.close()
sock.close()
