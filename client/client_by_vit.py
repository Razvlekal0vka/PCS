import sys
import socket

from requests import get, delete, post


def continue_work():
    print('Do you wish to continue? (y/n)')
    answer = str(input())
    if answer == 'n':
        print('end')
        sys.exit()
    elif answer not in ('y', 'n'):
        while answer not in ('y', 'n'):
            print('Do you wish to continue? (y/n)')
            answer = str(input())
            sending_a_file()
    else:
        sending_a_file()


def sending_a_file():
    print('Write the full address of the uploaded file')
    address_of_the_uploaded_file = str(input())
    print('In which folder do you want to save it')

    # In_which_folder_it_will_save = str(input()) - то, где должен храниться файл

    name_file = list(address_of_the_uploaded_file.split('/'))[-1]

    print(post('http://127.0.0.1:8081/api/user_file/new_file', json={'username': username,
                                                                     'password': password,
                                                                     'friend_username': '',
                                                                     'new_file': name_file,
                                                                     'delete_file': '',
                                                                     'email': '',
                                                                     'accessible_file': ''}).json())

    ip = "localhost"
    port = 9999

    # создаём сокет для подключения
    sock = socket.socket()
    sock.connect((ip, port))

    # запрашиваем имя файла и отправляем серверу
    f_name = address_of_the_uploaded_file  # input('File to send: ')
    sock.send((bytes(f_name, encoding='UTF-8')))

    # открываем файл в режиме байтового чтения
    f = open(f_name, "rb")

    # читаем строку
    l = f.read(1024)

    while (l):
        # отправляем строку на сервер
        sock.send(l)
        l = f.read(1024)

    f.close()
    sock.close()

    # тут надо ловить ошибку на сервере и ее дублировать здесь, вряд ли сейчас сделаю

    continue_work()


print('Your username:')
username = str(input())
print('Your password:')
password = str(input())

answer = post('http://127.0.0.1:8081/api/user_verification/account_login', json={'id': '',
                                                                                 'name': '',
                                                                                 'username': username,
                                                                                 'password': password,
                                                                                 'phone': '',
                                                                                 'email': '',
                                                                                 'activation_code': ''}).json()
print(answer)

if answer == True:
    print('You in system')
else:
    print('error in username or password')
    while answer != True:
        print('Your username:')
        username = str(input())
        print('Your password:')
        password = str(input())
        answer = post('http://127.0.0.1:8081/api/user_verification/account_login', json={'id': '',
                                                                                         'name': '',
                                                                                         'username': username,
                                                                                         'password': password,
                                                                                         'phone': '',
                                                                                         'email': '',
                                                                                         'activation_code': ''}).json()
        if answer == True:
            print('You in system')

print('Do you wish to continue? (y/n)')
answer = str(input())
if answer == 'n':
    print('end')
    sys.exit()
elif answer not in ('y', 'n'):
    while answer not in ('y', 'n'):
        print('Do you wish to continue? (y/n)')
        answer = str(input())
        sending_a_file()
else:
    sending_a_file()
