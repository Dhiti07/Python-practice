# queue using list
class QueueUsingList:
    def __init__(self):
        self.__queue = []
    def size(self):
        return len(self.__queue)
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self,data):
        self.__queue.append(data)
        return f"Added {data} to the Queue"
    def front(self):
        if(self.size()==0):
            print("Queue is Empty")
            return None
        return self.__queue[0]
    def dequeue(self):
        if(self.size()==0):
            print("Queue is Empty")
            return None
        return self.__queue.pop(0)
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
