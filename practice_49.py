# Binary Tree Node
from collections import deque

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

def print_binary_tree(root):
    if(root == None):
        return
    print(root.data, end = ":")
    if(root.left is not None):
        print(f"L->{root.left.data}", end = " ,")
    else:
        print("L->None",end = ",")
    
    if(root.right is not None):
        print(f"R->{root.right.data}")
    else:
        print("R->None")

    print_binary_tree(root.left)
    print_binary_tree(root.right)
print_binary_tree(root)

def take_input():
    data = int(input("Enter the data for the Node: "))
    if(data == -1):
        return None
    
    node = BinaryTreeNode
    node.left = take_input()
    node.right = take_input()

    return node
root = take_input()

def take_input_level_wise():
    data = int(input("Enter the data for input"))
    if(data == -1):
        return None
    root = BinaryTreeNode(data)
    queue = deque([root])

    while len(queue)!=0:
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter the left child for {current_node}"))
        if(left_child_data != -1):
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_node
            queue.append(left_node)
        right_child_data = int(input(f"Enter right child for {current_node.data}"))
        if(right_child_data != -1):
            right_node = BinaryTreeNode(right_child_data)
            current_node.right  = right_node
            queue.append(right_node)

    return root
             