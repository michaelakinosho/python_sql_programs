# Credit: source of solution is AlgoExpert provided solution
class Node:
    def __iniit__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, name):
        self.children.append(Node(name))
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array