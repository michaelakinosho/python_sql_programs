
def factors(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k

#for n in factors(n=100):
#    print(n)

n = 100
squares,factors ={k:k*k for k in range(1,n+1)},\
    {k:k for k in range(1,n+1) if n%k==0}
print(squares)
#print(factors)

squares,factors =[(k*k for k in range(1,n+1)),\
    (k for k in range(1,n+1) if n%k==0)]
#print(squares)
#print(factors)

#n = int(input("Enter a  positive number: "))
#total = sum(k*k for k in range(1,n))
#print(total)
