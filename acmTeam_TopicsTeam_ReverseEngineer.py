n,m = [int(x) for x in input().split()]
maxi = 0
cnt = 0
inp = [input() for _ in range(n)]
for i in range(0,n):
    for j in range(i+1,n):
        #This is where the digits comparsion is happening between each teammate for one topic at a time
        set_bit = bin(int(inp[i],2) | (int(inp[j],2))).count("1")
        print(set_bit)
        if set_bit>maxi:
            maxi = set_bit
            cnt = 1
        elif set_bit == maxi:
            cnt+=1
print(maxi)
print(cnt)
