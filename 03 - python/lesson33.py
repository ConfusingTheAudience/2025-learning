# DATES & TIMES

# 58. datetime

import datetime

date = datetime.date(2025, 1, 2)
# date(year, month, day)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
# time(hour, minutes, seconds)
now = datetime.datetime.now()

now = now.strftime('%H:%M:%S %d-%m-%Y')
# strfttime(format specifiers)
# we can check full list of format specifiers in documentation

print(now)