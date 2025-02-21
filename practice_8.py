class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node in the BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Function for In-Order Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Function for Pre-Order Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Function for Post-Order Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Construct the given BST
root = Node(25)
root = insert(root, 15)
root = insert(root, 50)
root = insert(root, 10)
root = insert(root, 22)
root = insert(root, 35)
root = insert(root, 70)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 24)
root = insert(root, 31)
root = insert(root, 44)
root = insert(root, 66)
root = insert(root, 90)

# Print traversals
print("In-order traversal:")
inorder(root)
print("\nPre-order traversal:")
preorder(root)
print("\nPost-order traversal:")
postorder(root)
