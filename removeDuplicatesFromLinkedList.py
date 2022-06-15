
class LinkedList:
    def __init__(self, value):
            self.value = value
            self.next = None
    def addMany(self, values):
            
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currentNode = linkedList
    while currentNode is not None:
        nextUniqueNode = currentNode.next
        while nextUniqueNode is not None and nextUniqueNode.value == currentNode.value:
            nextUniqueNode = nextUniqueNode.next

        currentNode.next = nextUniqueNode
        currentNode = nextUniqueNode

    return linkedList

dictList = {
    "head": "1",
    "nodes": [{"id": "1", "next": "1-2", "value": 1}, {"id": "1-2", "next": "1-3", "value": 1}, {"id": "1-3", "next": "2", "value": 1}, {"id": "2", "next": "3", "value": 3}, {"id": "3", "next": "3-2", "value": 4}, {"id": "3-2", "next": "3-3", "value": 4}, {"id": "3-3", "next": "4", "value": 4}, {"id": "4", "next": "5", "value": 5}, {"id": "5", "next": "5-2", "value": 6}, {"id": "5-2", "next": None, "value": 6}]}

dictList2 = {
    "head": "1",
    "nodes": [
      {"id": "1", "next": None, "value": 1}
    ]
  }

dictList3 = {
    "head": "-5",
    "nodes": [
      {"id": "-5", "next": "-1", "value": -5},
      {"id": "-1", "next": "-1-2", "value": -1},
      {"id": "-1-2", "next": "-1-3", "value": -1},
      {"id": "-1-3", "next": "5", "value": -1},
      {"id": "5", "next": "5-2", "value": 5},
      {"id": "5-2", "next": "5-3", "value": 5},
      {"id": "5-3", "next": "8", "value": 5},
      {"id": "8", "next": "8-2", "value": 8},
      {"id": "8-2", "next": "9", "value": 8},
      {"id": "9", "next": "10", "value": 9},
      {"id": "10", "next": "11", "value": 10},
      {"id": "11", "next": "11-2", "value": 11},
      {"id": "11-2", "next": None, "value": 11}
    ]
  }


def runProgram(linkedList):
    
    tempLinkedList = []
    for node in linkedList["nodes"]:
        #print(node)
        tempLinkedList.append(node["value"])

    print(tempLinkedList)

    newLinkedList = LinkedList(tempLinkedList[0]).addMany(tempLinkedList)

    newLinkedList = removeDuplicatesFromLinkedList(newLinkedList)

    print(newLinkedList.getNodesInArray())


runProgram(dictList)

runProgram(dictList2)

runProgram(dictList3)