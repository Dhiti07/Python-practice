# Traversals of Trees

def preorder_traversal(root):
    if(root!=None):
        return
    print(root.data,end = " ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if(root!=None):
        return 
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end = " ")

def inorder_traversal(rrot):
    if(root!=None):
        return
    inorder_traversal(root.left)
    print(root.data, end = " ")
    inorder_traversal(root.right)
    