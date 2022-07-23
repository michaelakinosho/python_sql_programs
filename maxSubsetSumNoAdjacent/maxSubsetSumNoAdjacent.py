# Credit: source of solution is AlgoExpert provided solution
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[i] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i -2] + array[i])
    return maxSums

# Credit: source of solution is AlgoExpert provided solution
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first + array[i], second)
        first = second
        second = current
    return second