from itertools import permutations

A,B = input().split(" ")
A = list(A)
A.sort()
B = int(B)
#print(A)
#print(B)
#lst = [(*permutations(A,B))]
#print(lst)
y = ""
for x in permutations(A,B):
    #print(type(x))
    print(''.join(x))

print(" ")
#Alternate implementation
#A,B = input().split()
#print(*[''.join(i) for i in permutations(sorted(A),int(B))],sep = '\n')
