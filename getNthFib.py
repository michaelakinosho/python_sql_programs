def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
      
    numList = [0,1]
    for x in range(2,n):
        temp = numList[0]
        numList[0] = numList[1]
        numList[1] = temp + numList[0]
        print((numList))
        getNthFib(n)
    
getNthFib(4)