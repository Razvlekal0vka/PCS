import csv
import os
from datetime import datetime, date
from flask import jsonify
from flask_restful import Resource
from .users_parser import parser


def read_user_data():
    print('reading user data')
    data = []
    with open('analysis_and_control_of_user_data/data/users_data.csv', 'r', newline='') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['id', 'name', 'username', 'password', 'phone', 'email', 'activation_code']:
                data.append(row)
    return data


def read_key_data():
    print('reading data by keys')
    data = []
    with open('analysis_and_control_of_user_data/data/activation_keys.csv') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']:
                data.append(row)
    return data


def write_key_data(key_data):
    with open('analysis_and_control_of_user_data/data/activation_keys.csv', 'w', newline="") as csvfile:
        fieldnames = ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(key_data)


def write_user_data(user_data):
    with open('analysis_and_control_of_user_data/data/users_data.csv', 'w', newline="") as csvfile:
        fieldnames = ['id', 'name', 'username', 'password', 'phone', 'email', 'activation_code']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_data)


def checking_code_for_expiration(key):
    print('check key for expiration')
    for key_data in read_key_data():
        if key_data[0] == key:
            data_start, data_end = key_data[1], key_data[2]
            current_datetime = datetime.now()
            start_time = data_start.split('.')

            now_time = str(current_datetime.day) + '.' + str(current_datetime.month) + '.' + str(current_datetime.year)
            now_time = now_time.split('.')

            end_time = data_end.split('.')

            if date(int(start_time[2]), int(start_time[1]), int(start_time[0])) > date(int(now_time[2]),
                                                                                       int(now_time[1]),
                                                                                       int(now_time[0])):
                return 'activation code is not active yet'
            if date(int(end_time[2]), int(end_time[1]), int(end_time[0])) < date(int(now_time[2]), int(now_time[1]),
                                                                                 int(now_time[0])):
                print('activation code expired')
                return 'activation code expired'
            else:
                print('everything is fine')
                return 'everything is fine'


def write_new_user_data(id):
    with open(f'C://PCS/server/users/{id}/user_data/data.csv', 'w', newline="") as csvfile:
        fieldnames = ['file', 'users_who_have_access']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()


class new_user(Resource):
    def post(self):
        print(' - new user registration')
        user_data = []
        args = parser.parse_args()
        max_id, usernames, phones, mails, activation_codes = 0, [], [], [], []
        available_key, code_flag = [], 0

        for user in read_user_data():
            if max_id < int(user[0]):
                max_id = int(user[0])

            usernames.append(user[2])
            phones.append(user[4])
            mails.append(user[5])
            activation_codes.append(user[6])

        for key_data in read_key_data():
            available_key.append(key_data[0])
            if args['activation_code'] == key_data[0] and key_data[3] != '':
                return jsonify('this activation code has already been used during registration')

        print('checking the parameters of the new user')
        if args['username'] in usernames:
            return jsonify('this login is already taken')
        elif args['phone'] in phones:
            return jsonify('this phone has already been used during registration')
        elif args['email'] in mails:
            return jsonify('this email address was already used during registration')
        elif args['activation_code'] in activation_codes and args['activation_code'] != '':
            return jsonify('this activation code has already been used during registration')
        else:
            if args['activation_code'] in available_key and args['activation_code'] not in activation_codes and \
                    args['activation_code'] != '':
                answer = checking_code_for_expiration(args['activation_code'])
                if answer != 'everything is fine':
                    return jsonify(answer)
                activation_code, code_flag = args['activation_code'], 1
            else:
                activation_code, code_flag = '', 2

            letters_ru = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЫыЭэЮюЯя'
            letters_en = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
            letters_sy_bad = '-ъь[]|/.,<>?&$%#'
            letters_sy_good = '_@'
            letters_nu = '0123456789'

            """проверка имени (ника, который будет отображаться в системе и у других пользователей)"""
            name = args['name']
            if len(name) > 2:
                for let in name:
                    if let in letters_ru or let in letters_en or let in letters_nu or let in letters_sy_good:
                        pass
                    else:
                        return jsonify('invalid characters in name')
            else:
                return jsonify('invalid name length')

            """проверка логина"""
            username = args['username']
            if len(name) > 10:
                for let in username:
                    if let in letters_ru or let in letters_en or let in letters_nu or let in letters_sy_good:
                        pass
                    else:
                        return jsonify('invalid characters in username')
            else:
                return jsonify('invalid username length')

            """проверка пароля"""
            password = args['password']
            if len(name) > 10:
                for let in password:
                    if let in letters_ru or let in letters_en or let in letters_nu or let in letters_sy_good:
                        pass
                    else:
                        return jsonify('invalid characters in password')
            else:
                return jsonify('invalid username password')

            """Проверка почты"""
            phone = args['phone']

            """Проверка телефона"""
            email = args['email']

            new_key_data = []
            for key_data in read_key_data():
                if key_data[0] == activation_code and key_data[3] == '':
                    new_key_data.append({'activation_code': key_data[0], 'start_of_activation': key_data[1],
                                         'date_of_the_end_activation': key_data[2], 'id': max_id + 1})
                else:
                    new_key_data.append({'activation_code': key_data[0], 'start_of_activation': key_data[1],
                                         'date_of_the_end_activation': key_data[2], 'id': key_data[3]})
            write_key_data(new_key_data)

            user_data.append({'id': max_id + 1,
                              'name': name,
                              'username': username,
                              'password': password,
                              'phone': phone,
                              'email': email,
                              'activation_code': activation_code})

            print('user data record')
            with open('analysis_and_control_of_user_data/data/users_data.csv') as File:
                reader = csv.reader(File, delimiter=';', quotechar=',',
                                    quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if row != ['id', 'name', 'username', 'password', 'phone', 'email', 'activation_code']:
                        user_data.append({'id': row[0],
                                          'name': row[1],
                                          'username': row[2],
                                          'password': row[3],
                                          'phone': row[4],
                                          'email': row[5],
                                          'activation_code': row[6]})

            print('key data update')
            write_user_data(user_data)

            id = str(max_id + 1)
            os.mkdir(f"C://PCS")
            os.mkdir(f"C://PCS/server")
            os.mkdir(f"C://PCS/server/users")
            os.mkdir(f"C://PCS/server/users/{id}")
            os.mkdir(f"C://PCS/server/users/{id}/files")
            os.mkdir(f"C://PCS/server/users/{id}/user_data")

            write_new_user_data(id)

            if code_flag == 1:
                print('account successfully created with activation code')
                return jsonify('account successfully created with activation code')
            print('account successfully created without activation code')
            return jsonify('account successfully created without activation code')
