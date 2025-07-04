# stack using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class StackUsingLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    def push(self,data):
        newNode = Node(data)
        self.len +=1
        if(self.head == Node):
            self.head = newNode
            return f"Added {data} to the stack"
        newNode.next = self.head
        self.head = newNode
        return f"Added {data} to the stack"
    def top(self):
        if(self.head is None or self.len == 0):
            return "Stack is Empty, no top element"
        return self.head.data
    def pop(self):
        if(self.head is None or self.len == 0):
            return "Stack is Empty"
        dataAtTop = self.head.data
        self.head = self.head.next
        self.len -=1
        return dataAtTop
    
    def size(self):
        return self.len
    def isEmpty(self):
        return self.len == 0
myStack = StackUsingList()

print(myStack.is_empty())
print(myStack.push(1))
print(myStack.push(2))
print(myStack.push(3))
print(myStack.push(4))
print(myStack.push(5))
print(myStack.is_empty())
print(myStack.pop())
print(myStack.is_empty())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())
print(myStack.top())
