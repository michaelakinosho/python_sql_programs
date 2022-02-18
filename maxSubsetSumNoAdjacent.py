#Based on AlgoExpert Solution
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first + array[i], second)
        first = second
        second = current
    return second

array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))