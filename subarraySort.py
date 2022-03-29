from re import I, sub


def subarraySort(array):

    myLen = len(array)
    arrayIndices = [-1,-1]
    arraySort = list()
    for i in range(0, len(array)):
        arraySort.append(array[i])
        
    arraySort.sort()
    print(array)
    print(arraySort)

    i = 0
    while i < myLen:
        if array[i] != arraySort[i]:
            arrayIndices[0] = i
            break
        i += 1
          
    i = myLen -1
    while i > 0:
        if array[i] != arraySort[i]:
            arrayIndices[1] = i
            break
        i -= 1
    
    return arrayIndices

myList = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subarraySort(myList))

myList = [0,1]
print(subarraySort(myList))

myList = [1,0]
print(subarraySort(myList))