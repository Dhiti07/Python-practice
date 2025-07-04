# Queue using linked list
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    def size(self):
        return self.len
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self,data):
        newNode = Node(data)
        self.len += 1
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return f"Added to the end"
    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.head.data
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return None
        self.len -=1
        dataToBeReturned = self.head.data
        self.head = self.head.next
        if(self.head == None):
            self.tail = None
        return dataToBeReturned
    
Q = QueueUsingList()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
print(Q.size())
print(Q.isEmpty())  
print(Q.front())
print(Q.dequeue())
print(Q.dequeue())
print(Q.front())

