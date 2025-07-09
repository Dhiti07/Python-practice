# Taking input for trees

from practice_46 import TreeNode, print_tree

def take_input():
    data = int(input("Enter the data for the Nodes"))
    node = TreeNode(data)
    num_children = int(input(f"Enter the no. of childer for {data}"))
    for eachchild in range(num_children):
        child = take_input()
        node.children.append(child)
    return node
root = take_input()
print_tree(root)
