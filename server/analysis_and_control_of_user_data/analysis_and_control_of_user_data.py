import csv

from flask import jsonify
from flask_restful import Resource
from .users_parser import parser


class new_user(Resource):
    def post(self):
        user_data = []
        args = parser.parse_args()
        denominations, data = ['id', 'name', 'username', 'password', 'phone', 'email', 'activation_code'], []
        max_id, usernames, phones, mails, activation_codes = 0, [], [], [], []
        with open('analysis_and_control_of_user_data/data/users_data.csv', 'r', newline='') as File:
            reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row != denominations:
                    if False:
                        pass
                    else:
                        data.append({'id': row[0],
                                     'name': row[1],
                                     'username': row[2],
                                     'password': row[3],
                                     'phone': row[4],
                                     'email': row[5],
                                     'activation_code': row[6]})
                        if max_id < int(row[0]):
                            max_id = int(row[0])

                        usernames.append(row[2])
                        phones.append(row[4])
                        mails.append(row[5])
                        activation_codes.append(row[6])

        if args['username'] in usernames:
            return jsonify('this login is already taken')
        elif args['phone'] in phones:
            return jsonify('this phone has already been used during registration')
        elif args['email'] in mails:
            return jsonify('this email address was already used during registration')
        elif args['activation_code'] in activation_codes and args['activation_code'] != '':
            return jsonify('this activation code has already been used during registration')
        else:
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

            """Проверка кода активации"""
            activation_code = args['activation_code']

            key_data = []
            ack = 0

            with open('analysis_and_control_of_user_data/data/activation_keys.csv') as File:
                reader = csv.reader(File, delimiter=';', quotechar=',',
                                    quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if row != ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']:
                        print(row, row[0], '-', row[3], '-',  activation_code, '-')
                        if row[0] == activation_code and row[3] == '':
                            print('-==-=-=-=-=-=-=-=-=-=-=-=-')
                            ack = 1
                            key_data.append({'activation_code': row[0], 'start_of_activation': row[1],
                                             'date_of_the_end_activation': row[2], 'id': max_id + 1})
                        else:
                            key_data.append({'activation_code': row[0], 'start_of_activation': row[1],
                                             'date_of_the_end_activation': row[2], 'id': row[3]})
            print(key_data)
            with open('analysis_and_control_of_user_data/data/activation_keys.csv', 'w', newline="") as csvfile:
                fieldnames = ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(key_data)

            if ack == 1:
                print('1')
                user_data.append({'id': max_id + 1,
                                  'name': name,
                                  'username': username,
                                  'password': password,
                                  'phone': phone,
                                  'email': email,
                                  'activation_code': activation_code})
            elif ack == 2:
                print('2')
                user_data.append({'id': max_id + 1,
                                  'name': name,
                                  'username': username,
                                  'password': password,
                                  'phone': phone,
                                  'email': email,
                                  'activation_code': ''})

            with open('analysis_and_control_of_user_data/data/users_data.csv') as File:
                reader = csv.reader(File, delimiter=';', quotechar=',',
                                    quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if row != denominations:
                        user_data.append({'id': row[0],
                                          'name': row[1],
                                          'username': row[2],
                                          'password': row[3],
                                          'phone': row[4],
                                          'email': row[5],
                                          'activation_code': row[6]})

            print(user_data)
            print('===========')
            print(key_data)
            with open('analysis_and_control_of_user_data/data/users_data.csv', 'w', newline="") as csvfile:
                fieldnames = denominations
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(user_data)

            if ack == 1:
                return jsonify('account successfully created with activation code')
            return jsonify('account successfully created without activation code')


class adding_an_activation_code(Resource):
    def post(self):
        pass
