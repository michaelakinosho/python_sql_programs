class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }
    addFront(val) {
        // Creating a new node object with the value provided
        let new_node = new Node(val);
        // Checking to see if the current list does not have a head node (if the list is empty)
        // If the list is empty, place the new node as the head
        if(!this.head) {
            this.head = new_node;
            return this;
        }

        // If the list is not empty, assign the head to be the next node to the new node
        new_node.next = this.head;
        // Then finally assign the new_node to be the new head of the list
        this.head = new_node;
        return this;
    }

    removeFront() {
        // If the list is empty, nothing to remove, return null
        if (!this.head) {
            this.head = null;
            return this;
        }
        // If list is not empty, remove current head and make next node the head
        this.head = this.head.next;
        return this;
    }

    front() {
        // If list is empty, no data to return, return null
        if (!this.head) {
            return null;
        }
        // If list is not empty, return data of current head node
        return this.head.data;
    }

    nextnode(next_node) {
        if (this.front() == null) {
            return null;
        }
        if (!this.head.next) {
            return null;
        }
    }

    contains(val){
        // Initialize variable to hold node
        let runner = this.head
        // Iterate through list to determine if value exist in any node
        while(runner !== null) {
            // if found then return true and stop, otherwise eventually return false
            if(runner.data === val){
                return true;
            }
            runner = runner.next;
        }
        return false;

    }

    length() {
        // Initialize variable to hold node
        let runner = this.head;
        // Iterate through list until next node is null
        let counter = 0
        while(runner) {
            // With each pass through the WHILE loop increae counter by one, until next runner is null 
            counter++
            runner = runner.next
        }
        return counter;
    }

    display() {
        // If linked list is empty return false
        if (this.front() === null) {
            return null;
        }
        // Since linked list is not empty
        // Initialize runner variable to head node
        // Pass value to myList
        let runner = this.head;
        let myList = runner.data
        runner = runner.next
        while(runner) {
            // Since next is not empty, pass value of node to myList variable
            myList = myList + ", " + runner.data
            runner = runner.next
        }
        return "[" + myList + "]";
    }

    findSum() {
        // We first have to tell our train attendant that we want to start at the front of the train
        let runner = this.head
        let sum = 0
        // Since a Linked List does not know how many nodes is within it, we will not be able to use a for loop to iterate, instead we'll use a while
        // Also we need to tell them when to stop otherwise they will just run off the end of the train
        while(runner !== null){
            // Since the runner is set to the current node, its value will be equal to the value of the node they are currently on
            sum += runner.data
            // Tell our attendant to move to the next car
            runner = runner.next;
        }
        return sum;
    }
}

mySLL = new LinkedList()
console.log(mySLL.contains(81))
console.log(mySLL.findSum())
console.log(mySLL.front())
mySLL.addFront(27)
mySLL.addFront(54)
mySLL.addFront(81)
console.log("Length of Singly Linked List is: ",mySLL.length())
console.log("Display the values in nodes:",mySLL.display())
console.log(mySLL.contains(81))
//console.log(mySLL.front())
//mySLL.removeFront()
console.log(mySLL.front())
console.log(mySLL.findSum())