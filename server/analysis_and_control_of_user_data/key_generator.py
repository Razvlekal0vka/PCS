import random
from datetime import datetime
import csv

code_length = 12  # only 12
"""==========================================="""
id = '' # '' или номер id
activation_date = 'now'  # 'now' or '05.08.2020'
end_date_of_work = '05.08.2030'
"""==========================================="""
letters = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz#@&%$'
code = ''

data = []
codes = []

with open('data/activation_keys.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row != ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']:
            data.append({'activation_code': row[0], 'start_of_activation': row[1], 'date_of_the_end_activation': row[2], 'id': row[3]})
            codes.append(row[0])
for n in range(12):
    s = str(letters[random.randint(0, len(letters) - 1)])
    code += s

while code in codes:
    code = ''
    for n in range(12):
        s = str(letters[random.randint(0, len(letters) - 1)])
        code += s

current_datetime = datetime.now()
print(f'user id - {id}')
print(f'code - {code}')
if activation_date == 'now':
    activation_date = str(
        str(current_datetime.day) + '.' + str(current_datetime.month) + '.' + str(current_datetime.year))
print(f'activation_date - {activation_date}')
print(f'end_date_of_work - {end_date_of_work}')

data.append({'activation_code': code,
         'start_of_activation': activation_date,
         'date_of_the_end_activation': end_date_of_work,
         'id': id})

with open('data/activation_keys.csv', 'w', newline="") as csvfile:
    fieldnames = ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
print("writing complete")