def minSwapsRequired(s):
    swaps = 0
    
    myList = list(s)
    
    i = 0
    s_length = len(s)
    j = s_length - 1
    
    while i < j:
        if myList[i] == myList[j]:
            pass
        elif myList[i] != myList[j]:
            k = j - 1
            while i < k:
                if myList[i] == myList[k]:
                    myList[j], myList[k] = myList[k], myList[j]
                    
                    swaps += 1
                    break
                k -= 1        
        i += 1
        j -= 1
        
    if myList[i] != myList[j]:
        return -1
    
    return swaps
    
s = "0100101"
print(minSwapsRequired(s))

s = "1110"
print(minSwapsRequired(s))

s = "101000"
print(minSwapsRequired(s))

s = "101"
print(minSwapsRequired(s))