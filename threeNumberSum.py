array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

def threeNumberSum(myArray, myTargetSum):
    myArray.sort()
    #print(myArray)
    myLen = len(myArray)
    myTriplets = []

    i = 0
    while i < myLen:
      
        j = i + 1
        while j < myLen:
        
            k = j + 1
            while k < myLen:
                if sum([myArray[i],myArray[j],myArray[k]]) == myTargetSum:
                    tempList = [myArray[i],myArray[j],myArray[k]]
                    myTriplets.append(tempList)
          
                k += 1
            j += 1
        i += 1
    #print(myTriplets)
    return myTriplets

threeNumberSum(array, targetSum)