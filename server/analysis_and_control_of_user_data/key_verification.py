from datetime import datetime
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

    if abs(flag_day - datetime.now().day) >= 1 and flag_verification == 0:
        flag_verification = 1

    if current_datetime.hour == 2 and current_datetime.minute == 59 and flag_verification == 1:
        flag_verification = 0
    if datetime.now().hour > 3 and datetime.now().hour < 1:
        time.sleep(3600)


if __name__ == '__main__':
    main()
