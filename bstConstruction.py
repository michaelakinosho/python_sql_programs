# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value: # So it can insert this new node on the left side
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else: # So it can insert this new node on the right side
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    
    def remove(self, value, parentNode=None):
        currentNode = self
        print(f'Trying to see the node values: {currentNode.value}')
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    print(f"Current node value is: {currentNode.value}")
                    currentNode.value = currentNode.right.getMinValue()
                    print(f"Current node value is: {currentNode.value}")
                    
                    currentNode.right.remove(currentNode.value, currentNode)
                    
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.right
                    else:
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
    
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
        
def inOrderTraverse(tree, array,i = 0):
    
    if tree is not None:
        
        inOrderTraverse(tree.left, array)
        
        array.append(tree.value)
        
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

myBST = BST(10)
myBST.insert(15)
myBST.insert(22)
myBST.insert(5)
myBST.insert(5)
myBST.insert(2)
myBST.insert(1)
print(inOrderTraverse(myBST,[]))

iBST = BST(1)
iBST.insert(2)
print(inOrderTraverse(iBST,[]))