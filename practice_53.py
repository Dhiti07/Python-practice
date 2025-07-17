#sorted list to bst tree
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_bst(root):
    if(root is None):
        return 
    print_bst(root.left)
    print(root.data, end = " ")
    print_bst(root.right)
def list_to_bst(l1):
    if(len(l1)==0):
        return None
    mid = len(l1)//2
    rootData = l1[mid]
    root = BSTNode(rootData)

    root.left = list_to_bst(l1[:mid])
    root.right = list_to_bst(l1[mid+1:])
    return root
if __name__ == "__main__":
    root = list_to_bst([1,2,3,4,5,6,7])
    print_bst(root)