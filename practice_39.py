from practice_34 import print_LL,take_input,LengthOfLL
# delete from the head

head = take_input()

def delete_from_start(head):
    if(head==None):
        return None
    newHead = head.next
    return newHead
print_LL(head)
head = delete_from_start(head)
print("After Deletion")
print_LL(head)

def delete_at_tail(head):
    if(head==None):
        return None
    temp = head
    while(temp.next.next is not None):
        temp = temp.next
    temp.next = None
    return head
head = delete_at_tail(head)
print_LL(head)
