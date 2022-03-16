def mergeOverlappingIntervals(intervals):
    arr_len = len(intervals)
    #print(arr_len)
    if arr_len == 1:
        return intervals
    
    i = 0
    while i < arr_len - 1:
        j = i + 1
        while j < arr_len:
            if intervals[i][0] > intervals[j][0]:
                print(intervals)
                tempInterval = intervals[j]
                intervals[j] = intervals[i]
                intervals[i] = tempInterval
                print(intervals)
            
            j += 1
            
        
        #intervals.pop(i)
        i += 1
        
    i = 0
    while i < arr_len - 1:
        j = i + 1
        while j < arr_len:
            if intervals[i][1] >= intervals[j][1]:
                #print(intervals)
                intervals.pop(j)
                arr_len -= 1
                j -= 1
            elif intervals[i][1] >= intervals[j][0]:
                #print(intervals)
                intervals[i][1] = intervals[j][1]
                intervals.pop(j)
                arr_len -= 1
                j -= 1
                
            j += 1
        i += 1

    return intervals

intervals = [[1,2]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 2],[3, 5],[4, 7],[6, 8],[9, 10]]
print(mergeOverlappingIntervals(intervals))

intervals = [[100,105],[1,104]]
print(mergeOverlappingIntervals(intervals))

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(mergeOverlappingIntervals(intervals))