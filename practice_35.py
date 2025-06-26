from practice_34 import Node, take_input, print_LL

def LengthOfLL(head):
    temp = head
    ans = 0
    while temp is not None:
        temp = temp.next
        ans += 1
    return ans
print("Length of Linked List:", LengthOfLL(head))

