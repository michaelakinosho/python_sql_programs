def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort(reverse = True)
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    myList = [0,[]]
    if arrayOne[0]-arrayTwo[0] == 0:
        myList[1] = [arrayOne[0],arrayTwo[0]]
        return(myList[1])
    
    myList[0] = abs(arrayOne[0]-arrayTwo[0])
    myList[1] = [arrayOne[0],arrayTwo[0]]
    i = 0
    while i < len(arrayOne):
        j = 0
        if i == 0:
            j = 1
        while j < len(arrayTwo):
            if myList[0] > abs(arrayOne[i]-arrayTwo[j]):
                myList[0] = abs(arrayOne[i]-arrayTwo[j])
                myList[1] = [arrayOne[i],arrayTwo[j]]

            j += 1
        i += 1
    return myList[1]
  
arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]

print(smallestDifference(arrayOne, arrayTwo))
