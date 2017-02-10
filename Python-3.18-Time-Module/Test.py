import time, calendar
a = time.localtime(time.time())
print(time.localtime(time.time()))
print(a.tm_mon," ",a.tm_hour)
print(time.asctime(time.localtime(time.time())))
print(calendar.month(1991, 12))