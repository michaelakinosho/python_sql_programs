#Utilizing solution obtained from Hackerrank member, mine only scored 24 points
N,M = [int(_) for _ in input().split(' ')]

Is = {}
for m in range(M) :
    a,b,k = [int(_) for _ in input().strip().split(' ')]
    if k == 0 :
        continue

    # if a in Is:
    #     print("This is pre-a: ", Is[a])

    Is[a] = Is.get(a,0) + k
    # print("This is post-a: ", Is[a])
    #
    # if b+1 in Is:
    #     print("This is pre-b: ", Is[b+1])

    Is[b+1] = Is.get(b+1,0) - k
    # print("This is post-b: ", Is[b+1])
    #
    # print(Is)

m,v = 0,0
#print(sorted(Is.values()))
for i in sorted(Is) :
    #print(i, Is[i])
    v += Is[i]
    if v > m :
        m = v

print(m)
