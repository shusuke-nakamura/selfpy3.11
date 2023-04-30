d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
try:
    print(d['pear'])
except KeyError as ke:
    print(ke.__class__, ':', ke)
print(d.get('pear', '×'))
print(d.pop('melon', '×'))
print(d.popitem())
print(d)
