
def factors(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k

for n in factors(n=100):
    print(n)
