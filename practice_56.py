# Creating a BST class
class Node:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.insertHelper(data,self.root)
    def insertHelper(self,data,node):
        if(node is None):
            newNode = Node(data)
            return newNode 
        if(data<self.root.data):
            node.left = self.insertHelper(data, node.left)
        else:
            node.right = self.insertHelper(data, node.right)
        return node
    def delete(self,data):
        pass
    def search(self,data):
        return self.searchHelper(data,self.root)
    
    def searchHelper(self,data,root):
        if(root is None):
            return False
        if(root.data == data):
            return True
        if(data<root.data):
            return self.searchHelper(data,root.left)
        else:
            return self.searchHelper(data,root.right)