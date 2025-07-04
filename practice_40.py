from practice_34 import print_LL,LengthOfLL,take_input

# delete node by value
head = take_input()
def delete_by_value(head, value):
    temp = head
    if(head == None):
        return None
    while(temp is not None and temp.next.data != value):
        temp = temp.next
    temp.next = temp.next.next
    return head
head = delete_by_value(head,30)
print_LL(head)