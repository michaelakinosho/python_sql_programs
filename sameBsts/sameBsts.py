# Credit: source of solution is AlgoExpert provided solution
# def sameBsts(arrayOne, arrayTwo):
#     if len(arrayOne) != len(arrayTwo):
#         return False
    
#     if len(arrayOne) == 0 and len(arrayTwo) == 0:
#         return True
    
#     if arrayOne[0] != arrayTwo[0]:
#         return False
    
#     leftOne = getSmaller(arrayOne)
#     leftTwo = getSmaller(arrayTwo)
#     rightOne = getBiggerOrEqual(arrayOne)
#     rightTwo = getBiggerOrEqual(arrayTwo)
    
#     return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)
    
    
# def getSmaller(array):
#     smaller = []
#     for i in range(1, len(array)):
#         if array[i] < array[0]:
#             smaller.append(array[i])
#         return smaller
    
# def getBiggerOrEqual(array):
#     biggerOrEqual = []
#     for i in range(1, len(array)):
#         if array[i] >= array[0]:
#             biggerOrEqual.append(array[i])
#         return biggerOrEqual
    
# Credit: source of solution is AlgoExpert provided solution
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo
    
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False
    
    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)
    
    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)
    
    return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startingIdx, minVal):
    # Find the index of the first time smaller value after the startingIdx.
    # Make sure that this value is greater than or equal to the minVal,
    # which is te value of the previous parent node in the BST. If it
    # isn't, then that value is located in the left subtree of the
    # previous parent node
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    # Find the index of the first bigger/equal value after the startingIdx.
    # Make sure that this value is smaller than maxVal, which is the value
    # of the previous parent node in the BST. If it isn't, then that value
    # is located in the right subtree of the previous parent node.
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1