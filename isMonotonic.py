def isMonotonic(array):
    # Write your code here.
    monotonic = True
    myLen = len(array)

    if myLen < 3:
      return monotonic
    
    trend = "even"
    if array[0] > array[1]:
        trend = "down"
    elif array[0] < array[1]:
        trend = "up"
    
    temp = "even"
    for i in range(1, len(array)-1):
        if array[i] > array[i+1]:
            temp = "down"
        elif array[i] < array[i+1]:
            temp = "up"
        
        if trend == "even" and temp != "temp":
            trend = temp
        
        if trend == "up" and temp == "down":
            monotonic = False
            break
        elif trend == "down" and temp == "up":
            monotonic = False
            break
        
    return monotonic
  
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))