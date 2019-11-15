N,M = [int(_) for _ in input().split(' ')]

Is = {}
for m in range(M) :
    a,b,k = [int(_) for _ in input().strip().split(' ')]
    if k == 0 :
        continue
    Is[a] = Is.get(a,0) + k
    print(Is[a])
    Is[b+1] = Is.get(b+1,0) - k

print(Is)
m,v = 0,0
print(sorted(Is.values()))
for i in sorted(Is) :
    print(i, Is[i])
    v += Is[i]
    if v > m :
        m = v

print(m)
