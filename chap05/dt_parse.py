import datetime

d1 = datetime.datetime.strptime('2019/8/5 11:37:25', '%Y/%m/%d %H:%M:%S')
print(d1)
d2 = datetime.datetime.fromisoformat('2019-08-05 11:37:25+09:00')
print(d2)
