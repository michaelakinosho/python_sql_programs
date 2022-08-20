# Credit: source of solution is AlgoExpert provided solution
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

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode
        print(f"Current node: {currentNode.value}, valueOne: {valueOne}, valueTwo: {valueTwo} ")

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
        print(f"What is nodeOne: {nodeOne}, What is nodeTwP {nodeTwo}, What is carry {carry}")
    print("\n")
    tempPointer = newLinkedListHeadPointer.next
    while tempPointer is not None:
        print(tempPointer.value)
        tempPointer = tempPointer.next
    return newLinkedListHeadPointer.next

print(sumOfLinkedLists(LinkedList(9).addMany([4,7,1,2,5]), LinkedList(2).addMany([4,])))