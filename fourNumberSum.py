array = [7,6,4,-1,1,2]
targetSum = 16

def fourNumberSum(myArray, myTargetSum):
    #myArray.sort()
    #print(myArray)
    myLen = len(myArray)
    myQuadruplets = []

    i = 0
    while i < myLen:
      
        j = i + 1
        while j < myLen:
        
            k = j + 1
            while k < myLen:

                l = k + 1
                while l < myLen:

                    if sum([myArray[i],myArray[j],myArray[k],myArray[l]]) == myTargetSum:
                        tempList = [myArray[i],myArray[j],myArray[k],myArray[l]]
                        myQuadruplets.append(tempList)
                    l += 1
                k += 1
            j += 1
        i += 1
    #print(myQuadruplets)
    return myQuadruplets

print(fourNumberSum(array, targetSum))