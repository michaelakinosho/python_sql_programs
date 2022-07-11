# Credit: source of solution is AlgoExpert provided solution
from fileinput import close


# def apartmentHunting_solution1(blocks, reqs):
#     maxDistancesAtBlocks = [float("-inf") for block in blocks]
#     for i in range(len(blocks)):
#         for req in reqs:
#             closetReqDistance = float("inf")
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                     closetReqDistance = min(closetReqDistance, distanceBetween(i, j))
#             maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closetReqDistance)
#     return getIdxAtMinValue(maxDistancesAtBlocks)

def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)

def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for blocks in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlocks = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlocks)
    return maxDistancesAtBlocks

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue 
        

def distanceBetween(a, b):
    return abs(a - b)

# blocks = [
#   {
#     "gym": False,
#     "school": True,
#     "store": False
#   },
#   {
#     "gym": True,
#     "school": False,
#     "store": False
#   },
#   {
#     "gym": True,
#     "school": True,
#     "store": False
#   },
#   {
#     "gym": False,
#     "school": True,
#     "store": False
#   },
#   {
#     "gym": False,
#     "school": True,
#     "store": True
#   }
# ]

# reqs = ["gym", "school", "store"]

# print(apartmentHunting(blocks,reqs))