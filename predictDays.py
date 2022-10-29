def predictDays(day, k):
    i = k
    idealDays = []
    status = False
    while i < len(day) - k:
        j, z = i - k, i + k
        while j < i:
            if day[j]>=day[j+1] and day[z]>=day[z-1]:
                status = True
            else:
                status = False
                break
            j += 1
            z -= 1
        
        if status == True:
            idealDays.append(i+1)
            status = False
        
        i += 1
    return idealDays

day = [3,2,2,2,3,4]
k = 2
print(predictDays(day, k))

day = [0,0,0,0,0]
k = 2
print(predictDays(day, k))