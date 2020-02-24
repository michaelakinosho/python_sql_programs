for i in range(1,int(input())):
    x = lambda t,s : t*pow(10,s)
    #print(x(i,i))
    for z in range(1,i+1):
        tt = 0
        for xx in range(0,z):
            tt += x(z,xx)
    print(tt)

for i in range(1,int(input())):
    print([1,22,333,4444,55555,666666,7777777,88888888,999999999][i-1])
