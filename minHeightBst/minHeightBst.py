# Credit: source of solution is AlgoExpert provided solution
def minHeightBst(array):
    return constructMinHeightsBst(array, 0, len(array) - 1)

# def minHeightBst(array):
#     return constructMinHeightsBst(array, None, 0, len(array) - 1)

# def constructMinHeightsBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2
#     valueToAdd = array[midIdx]
#     if bst is None:
#         bst.insert(valueToAdd)
#     else:
#         bst.insert(valueToAdd)
#     constructMinHeightsBst(array, bst, startIdx, midIdx - 1)
#     constructMinHeightsBst(array, bst, midIdx + 1, endIdx)
#     return bst

# def constructMinHeightsBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2
#     newBstNode = BST(array[midIdx])
#     if bst is None:
#         bst = newBstNode
#     else:
#         if array[midIdx] < bst.value:
#             bst.left = newBstNode
#             bst = bst.left
#         else:
#             bst.right = newBstNode
#             bst = bst.right
#     constructMinHeightsBst(array, bst, startIdx, midIdx - 1)
#     constructMinHeightsBst(array, bst, midIdx + 1, endIdx)
#     return bst

def constructMinHeightsBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightsBst(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightsBst(array, midIdx + 1, endIdx)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)