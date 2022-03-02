

def longestPeak(array):
    if len(array) < 3:
        return 0
    
    myList = []
    i = 0
    while i < len(array) - 1:
        direction = ""
        tempList = []
        j = i
        while j < len(array) - 1:
            if array[j] < array[j+1]:
                if direction == "" or direction == "up":
                    direction = "up"
                    tempList.append(array[j])
                else:
                    #myList.append(tempList)
                    #i += 1
                    break
            elif array[j] > array[j+1]:
                if direction == "up":
                    direction = "peak"
                    tempList.append(array[j])
                elif direction == "peak":
                    direction = "down"
                    tempList.append(array[j])
                elif direction == "down":
                    direction = "down"
                    tempList.append(array[j])
                else:
                    #myList.append(tempList)
                    #i += 1
                    break
            else:
                #myList.append(tempList)
                #i += 1
                break

            #myList.append(tempList)
            j += 1
        if array[j-1] > array[j]:
            if direction == "down":
                tempList.append(array[j])
        if len(tempList) > len(myList) and len(tempList) > 2:
            myList = tempList
        i += 1

    return myList
  

arr = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(arr))