data = ['い', 'ろ', 'は', 'に', 'ほ', 'へ', 'と', 'い', 'ろ']

print(data.index('い'))
print(data.index('い', 4))
try:
    print(data.index('い', 4, 7))
except ValueError as ve:
    print(ve.__class__, ":", ve)
print(data.index('い', -4, -1))
