class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Print elements of a BST in a range
def print_bst_in_range(root,low,high):
    if(root is None):
        return
    if(low<root.data):
        print_bst_in_range(root.left)
    if(low<=root.data<= high):
        print(root.data, end = " ")

    if(high> root.data):
        print_bst_in_range(root.right, low,high)
