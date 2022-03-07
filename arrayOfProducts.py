def arrayOfProducts(array):
    import math
    newArray = []
    i = 0
    while i < len(array):
        temp1, temp2 = array[0:i], array[i+1:len(array)]
        if 0 in temp1 or 0 in temp2:
            newArray.append(0)
            i += 1
            continue
        temp1.extend(temp2)
        newArray.append(math.prod(temp1))
        
        i += 1
    return newArray
  
array = [5,1,4,2]
print(arrayOfProducts(array))

array = [0,0,0,0]
print(arrayOfProducts(array))