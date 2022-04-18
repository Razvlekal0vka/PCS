from datetime import datetime, date
import csv
import time

flag_verification = 0
flag_day = datetime.now().day


# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)


def main():
    global flag_verification, flag_day
    current_datetime = datetime.now()

    # if abs(flag_day - datetime.now().day) >= 1 and flag_verification == 0:
    # flag_verification = 1

    if (current_datetime.hour == 2 and current_datetime.minute == 59 and flag_verification == 1) or True:
        flag_verification = 0
        admissible_id = []
        banned_id = []
        expired_id = []

        good_id = []

        f = open('data/banned_id.txt', 'r')
        banned_id = [line.strip() for line in f]
        f.close()

        with open('data/activation_keys.csv') as File:
            reader = csv.reader(File, delimiter=';', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                print(row)
                if row != ['activation_code', 'start_of_activation', 'date_of_the_end_activation', 'id']:
                    start_time = row[1].split('.')
                    end_time = row[2].split('.')
                    if date(int(start_time[2]), int(start_time[1]), int(start_time[0])) <= date(int(end_time[2]), int(end_time[1]), int(end_time[0])):
                        good_id.append({'activation_code': row[0], 'start_of_activation': row[1], 'date_of_the_end_activation': row[2], 'id': row[3]})

    # if datetime.now().hour > 3 or datetime.now().hour < 1:
    # time.sleep(3600)


if __name__ == '__main__':
    main()
