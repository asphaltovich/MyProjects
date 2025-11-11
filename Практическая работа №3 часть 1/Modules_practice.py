import datetime
birthday = datetime.date(2017, 6, 1)

print(birthday)

import datetime
x = datetime.datetime.now()
print(x.year)

import datetime
x = datetime.datetime.now()

print(x.year,x.month,x.day)

import datetime
x = datetime.datetime.now()

print(x.year,x.month,x.day, x.hour, x.minute, x.second)

from datetime import date
birthday = date(2017, 6, 1)
print(birthday)

from datetime import date as h
birthday = h(2017, 6, 1)
print(birthday)
