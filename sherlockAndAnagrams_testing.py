from collections import Counter
s = input()
count = 0
for i in range(1,len(s)+1):
    a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
    #print(a)
    b = Counter(a)
    #print(b)
    for j in b:
        print(b[j])
        print(b[j]*(b[j]-1)/2)
        count+=b[j]*(b[j]-1)/2
    #print(int(count))
