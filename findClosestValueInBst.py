def findClosestValueInBst(tree, target):
    # Write your code here.
    print(target)
    myBST = BST(tree)
    print(myClass.value[0]['value'])
    
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = {"nodes": [{"id": "10", "left": "5", "right": "15", "value": 10},{"id": "15", "left": "13", "right": "22", "value": 15},{"id": "22", "left": null, "right": null, "value": 22},{"id": "13", "left": null, "right": "14", "value": 13},{"id": "14", "left": null, "right": null, "value": 14},{"id": "5", "left": "2", "right": "5-2", "value": 5},{"id": "5-2", "left": null, "right": null, "value": 5},{"id": "2", "left": "1", "right": null, "value": 2},{"id": "1", "left": null, "right": null, "value": 1}],"root": "10"}
target: 12

findClosestValueInBst(tree,target)