import csv
import os
from datetime import datetime, date
from flask import jsonify
from flask_restful import Resource
from .telegram_id_parser import parser


def read_telegram_id():
    print('reading telegram id')
    data = []
    with open('analysis_and_control_of_user_data/data/telegram_id_with_user_id.csv') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['telegram_id', 'pcs_id']:
                data.append(row)
    return data


def write_telegram_id(new_data):
    print('reading telegram id')
    with open('analysis_and_control_of_user_data/data/telegram_id_with_user_id.csv', 'w', newline="") as csvfile:
        fieldnames = ['telegram_id', 'pcs_id']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_data)


class telegram_id(Resource):
    def post(self):
        print(' - update telegram id')
        args = parser.parse_args()
        telegram_id, pcs_id = args['telegram_id'], args['pcs_id']
        data = []

        for user_data in read_telegram_id():
            if user_data[0] == telegram_id:
                data.append({
                    'telegram_id': telegram_id,
                    'pcs_id': pcs_id
                })
            else:
                data.append({
                    'telegram_id': user_data[0],
                    'pcs_id': user_data[1]
                })
        write_telegram_id(data)
        print('update telegram id - successful')
        return jsonify('True')