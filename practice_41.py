from practice_34 import take_input,LengthOfLL,print_LL

# search in a linked list by value
head = take_input()
def search_by_value(head,value):
    temp = head
    if(head==None):
        return None
    while(temp is not None):
        if(temp.data == value):
            print("value found")
            return
        else:
            temp = temp.next
    print("value not found")
    
search_by_value(head,2)