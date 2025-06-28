# insert at index

from practice_34 import print_LL,take_input,LengthOfLL
head = take_input()
def insert_at_index_recursively(head,data,index):
    if(index==0):
        return insert_at_index(head,data)
    if(head == None):
        print("Index is out of bounds")
        return head
    head.next = insert_at_index_recursively(head.next,data,index)
    return head
head = insert_at_index_recursively(head,35,3)
print("After Inserting at index")
print_LL(head)