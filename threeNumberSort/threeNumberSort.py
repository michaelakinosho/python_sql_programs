def threeNumberSort(array, order):
    myDict = {}
    for ord in order:
        myDict[ord] = array.count(ord)
    
    i = 0
    for k, v in myDict.items():
        for j in range(v):
            array[i] = k
            i += 1
        
    return array





array = [1,1,0,1,0,1,-1,0,-1,1]
order = [3,-1,0,1,2]
print(threeNumberSort(array, order))

array = []
order = [3,-1,0,1,2]
print(threeNumberSort(array, order))