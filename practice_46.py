# defining a tree
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

root = TreeNode(1)

child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
root.children.append(child1)
root.children.append(child2)
root.children.append(child3)
print(root.children[0].data)

def print_tree(root):
    if(root == None):
        return 
    print(root.data)
    for eachchild in root.children:
        print_tree(eachchild)
print_tree(root)