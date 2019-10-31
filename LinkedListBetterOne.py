class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    #Since I had a really hard time with this topic
    #Providing a lot of documentation
    def insert(self,head,data):
        if head==None:
            head=self
            head.data=data  #Pass data to the head at the beginning of implementing the Node
            head.next=None

        else:
            current=head
            while current.next:
                current=current.next
            current.next=Node(data)
        return head

    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
