def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

for y in fibonacci():
    print(y)
    if y > 1000000:
        break
