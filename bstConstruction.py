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
        
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def insertLeft(self, value):
        return self
      
    def insertRight(self, value):
        return self
    
    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

myBST = BST(10)
print(myBST.value)
myBST.insert(23)
myBST.insert(3)
print(myBST.right)
print(myBST.left)