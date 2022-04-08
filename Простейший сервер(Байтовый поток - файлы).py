import socket

# создаём сокет и связываем его с IP-адресом и портом

sock = socket.socket()
ip = '26.175.31.63'
port = 53210
sock.bind((ip, port))

# сервер ожидает передачи информации
sock.listen(10)

while True:
    # начинаем принимать соединения
    conn, addr = sock.accept()

    # выводим информацию о подключении
    print('connected:', addr)

    # получаем название файла
    name_f = (conn.recv(1024)).decode('UTF-8')

    # открываем файл в режиме байтовой записи в отдельной папке 'sent'

    while True:
        f = open(name_f, 'wb')

        # получаем байтовые строки
        bite_line = conn.recv(1024)

        # пишем байтовые строки в файл на сервере
        f.write(bite_line)

        if not bite_line:
            break

        f.close()

    conn.close()
    print('File received')
