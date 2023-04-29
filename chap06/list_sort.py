data = ['ぱんだ', 'うさぎ', 'こあら', 'とら']
data2 = [205, 13, 78, 50]
data3 = ['ぱんだ', 15, 'こあら']

data.sort()
print(data)
data2.sort()
print(data2)
try:
    data3.sort()
    print(data3)
except TypeError as te:
    print(te.__class__, ":", te)

data.sort(reverse=True)
print(data)
