def moveElementToEnd(array, toMove):
    # Write your code here.
    numCount = array.count(toMove)
    i = 0
    while i < numCount:
        array.remove(toMove)
        array.append(toMove)
        i += 1
    return array

array = [2,4,2,5,6,2,2]
toMove = 2

print(moveElementToEnd(array, toMove))