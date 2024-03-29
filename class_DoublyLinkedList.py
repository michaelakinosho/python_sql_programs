# This is an input class. Do not edit.
from venv import create
from click import argument


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
        

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
    
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        
    def getNodesInArray(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

dictList = {
  "nodes": [
    {"id": "1", "next": None, "prev": None, "value": 1},
    {"id": "2", "next": None, "prev": None, "value": 2},
    {"id": "3", "next": None, "prev": None, "value": 3},
    {"id": "4", "next": None, "prev": None, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    }
  ]
}


newDoublyLinkedList = DoublyLinkedList()

headNode = Node(1)
newDoublyLinkedList.setHead(headNode)
node = headNode
nodeToInsert = Node(2)
newDoublyLinkedList.insertAfter(node, nodeToInsert)
node = nodeToInsert
nodeToInsert = Node(24)
newDoublyLinkedList.insertAfter(node, nodeToInsert)
print(newDoublyLinkedList.getNodesInArray())
