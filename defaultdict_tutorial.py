from collections import defaultdict
d = defaultdict(list)

n,m = input().split(" ")
for _ in range(0,int(n)):
    d['A'].append(input())

for _ in range(0,int(m)):
    d['B'].append(input())

for _ in d['B']:
    print(_)
    s = str("")
    for x in d['A']:
        if _ == x:
            s = " " + x
    print(s)
print(len(d))
print(d['A'])
print(d['A'][0])
print('a' in d['A'])
