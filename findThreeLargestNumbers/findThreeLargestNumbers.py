# Credit: source of solution is AlgoExpert provided solution
def findThreeLargestNumbers(array):
    threeLargest = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)
    
def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]