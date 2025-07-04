class StackUsingList:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
        print(f"Pushed {data} into stack")
    def size(self):
        return len(self.stack)
    def is_empty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False
    def top(self):
        if(self.is_empty()):
            print("Stack is empty")
            return None
        return self.stack[-1] #gives the access of the last element
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
            return None
        return self.stack.pop()
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