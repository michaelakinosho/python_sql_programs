
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
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
                    print(f'Current node value is: {currentNode.value}')
                    currentNode.value = currentNode.right.getMinValue()
                    print(f'Current node value is: {currentNode.value}')
                    
                    currentNode.right.remove(currentNode.value, currentNode)
                    
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                elif parentNode.left == currentNode:
                    # This line of code is setting the old node to None
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    # This line of code is setting the old node to None
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
    
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

myBST = BST(10)
myBST.insert(5)
myBST.insert(15)
myBST.insert(2)
myBST.insert(5)
myBST.insert(13)
myBST.insert(22)
myBST.insert(1)
myBST.insert(14)
myBST.insert(12)
myBST.remove(10)
