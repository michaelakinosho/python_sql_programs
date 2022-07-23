from hashlib import new


# Credit: source of solution is AlgoExpert provided solution
# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)
#     return permutations

# def permutationsHelper(array, currentPermutation, permutations):
#     if not len(array) and len(currentPermutation):
#         permutations.append(currentPermutation)
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:]
#             newPermutation = currentPermutation + [array[i]]
#             permutationsHelper(newArray, newPermutation, permutations)

# Credit: source of solution is AlgoExpert provided solution
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)
            
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]