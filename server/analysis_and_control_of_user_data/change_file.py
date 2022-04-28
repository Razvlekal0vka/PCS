import csv
from datetime import datetime, date
from flask import jsonify
from flask_restful import Resource
from .data_parser import parser


def read_user_data():
    print('reading user data')
    data = []
    with open('analysis_and_control_of_user_data/data/users_data.csv', 'r', newline='') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['id', 'name', 'username', 'password', 'phone', 'email', 'activation_code']:
                data.append(row)
    return data


def read_user_data_of_file(id):
    print('reading data by file')
    data = []
    with open(f'C://Users/Razvlekal0vka/PycharmProjects/PCS/server/users/{id}/user_data/data.csv') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['file', 'users_who_have_access']:
                data.append(row)
    return data


def write_user_data_of_file(user_data, id):
    with open(f'C://Users/Razvlekal0vka/PycharmProjects/PCS/server/users/{id}/user_data/data.csv', 'w', newline="") as csvfile:
        fieldnames = ['file', 'users_who_have_access']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_data)


class change_file(Resource):
    def post(self):
        print('add new file')
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        new_file = args['new_file']
        delete_file = args['delete_file']
        accessible_file = args['accessible_file']
        friend_username = args['friend_username']
        new_file_data, names, flag = [], [], 0

        for user in read_user_data():
            if user[2] == username and user[3] == password:
                id = user[0]
                for data in read_user_data_of_file(id):
                    if data[0] != delete_file:
                        names.append(data[0])
                        new_file_data.append({'file': data[0],
                                              'users_who_have_access': data[1]})
                    else:
                        flag = 1
                        accessible_file = data[1]

                while new_file in names:
                    new_file = new_file.split('.')[0] + '(0)' + '.' + new_file.split('.')[1]

                new_file_data.append({'file': new_file,
                                      'users_who_have_access': accessible_file})
                write_user_data_of_file(new_file_data, id)
                if flag == 1:
                    return jsonify('True')
                return jsonify('no_such_file_exists')
        return jsonify('the user does not exist or the data entered is incorrect')
