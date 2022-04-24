import csv
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


class adding_an_activation_code(Resource):
    def post(self):
        print('adding an activation key by the user')
        args = parser.parse_args()
        username, password, activation_code = args['username'], args['password'], args['activation_code']
        for user_data in read_user_data():
            if user_data[2] == username and user_data[3] == password:
                if user_data[6] == activation_code:
                    return jsonify('you are already using this activation code')
                elif user_data[6] == '':
                    for key_data in read_key_data():
                        pass
                else:
                    return jsonify('you are already using another activation code')