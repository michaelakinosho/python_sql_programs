def firstDuplicateValue(array):

    if len(array) < 1:
        return -1
    
    arr_len = len(array)
    tempList = [0,arr_len]
    
    i = 0
    while i < arr_len - 1:
        if i >= tempList[1]:
            break
        
        num = array[i]
        if num != tempList[0]:
            tempArray = array[i+1:arr_len]
            if num in tempArray:
                tempIndex = tempArray.index(num)
                if tempIndex + i + 1 < tempList[1]:
                    tempList[1] = tempIndex + i + 1
                    tempList[0] = array[i]
                    print(tempList)
        
        i += 1
    if tempList[1] == arr_len:
        return -1
    
    #print(tempList)
    return tempList[0]
  
array = [2,1,5,2,3,3,4]
print(firstDuplicateValue(array))

array = [8, 20, 4, 12, 14, 9, 19, 17, 14, 20, 22, 9, 6, 15, 1, 15, 10, 9, 17, 7, 22, 17]
print(firstDuplicateValue(array))