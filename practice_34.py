# Taking input for a linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data, end="->")
        temp = temp.next
    print()
    return  
def take_input():
    value = int(input("Enter the value of Node: "))
    head = None
    tail = None  
    while value != -1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter the value of Node: "))
    return head 
def LengthOfLL(head):
    temp = head
    ans = 0
    while temp is not None:
        temp = temp.next
        ans += 1
    return ans
newhead = take_input()
print_LL(newhead)
print("Length of Linked List:", LengthOfLL(newhead))
