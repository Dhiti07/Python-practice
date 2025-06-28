from practice_34 import print_LL, take_input, LengthOfLL

# Insert at Index
def insert_at_index(head,data):
    if(index == 0):
        return insert_at_index(head,data)
    newNode = Node(data)
    temp = head
    count = 0

    while temp is not None and count < index - 1:
        temp = temp.next
        count+=1
    newNode.next = temp.next
    temp.next = newNode
    return head