from practice_34 import Node, take_input, print_LL

head = take_input()
print("Original Linked List:")
print_LL(head)

def insert_at_head(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode  
head = insert_at_head(head, 100)
print("After inserting 100 at head:")
print_LL(head)

def insert_at_tail(head,data):
    newNode = Node(data)
    if(head is None):
        return newNode
    temp = head
    while(temp.next!=None):
        temp = temp.next
    temp.next = newNode    

    return head 
head = insert_at_tail(head, 100)

print("After inserting 100 at tail:")
print_LL(head)
