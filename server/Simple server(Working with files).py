import socket

# создаём сокет и связываем его с IP-адресом и портом

sock = socket.socket()
ip = '127.0.0.1'
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
    downloads = 'C:/Users/User/PycharmProjects/PCS/server/downloads/'
    name_f = (conn.recv(1024)).decode('UTF-8')
    received_name_file = name_f[name_f.rfind('/') + 1:]
    name_f = downloads + name_f[name_f.rfind('/') + 1:]
    # открываем файл в режиме байтовой записи (в отдельной папке 'downloads')
    f = open(name_f, 'wb')

    while True:

        # получаем байтовые строки
        bite_line = conn.recv(1024)

        # пишем байтовые строки в файл на сервере
        f.write(bite_line)

        if not bite_line:
            break

    f.close()
    conn.close()

    print(f'{received_name_file} received to {downloads[:-1]}')
