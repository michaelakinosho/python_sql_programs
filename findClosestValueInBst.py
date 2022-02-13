
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = {"nodes": [{"id": "10", "left": "5", "right": "15", "value": 10},{"id": "15", "left": "13", "right": "22", "value": 15},{"id": "22", "left": None, "right": None, "value": 22},{"id": "13", "left": None, "right": "14", "value": 13},{"id": "14", "left": None, "right": None, "value": 14},{"id": "5", "left": "2", "right": "5-2", "value": 5},{"id": "5-2", "left": None, "right": None, "value": 5},{"id": "2", "left": "1", "right": None, "value": 2},{"id": "1", "left": None, "right": None, "value": 1}],"root": "10"}
target = 12

# Solution if from AlgoExpert, could not understand the implementation
# Decided to use solution from AlgoExpert
def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

findClosestValueInBst((tree),target)