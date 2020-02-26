from collections import defaultdict
d = defaultdict(list)

n,m = input().split(" ")
for _ in range(0,int(n)):
    d['A'].append(input())

for _ in range(0,int(m)):
    d['B'].append(input())

for _ in d['B']:
    #print(_)
    s = str("")
    if _ in d['A']
    i = 1
    for x in d['A']:
        if _ == x:
            s = s + " " + str(i)
        
        i += 1
    print(s.strip())
#print(len(d))
#print(d['A'])
#print(d['A'][0])
#print('a' in d['A'])
