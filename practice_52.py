# Construction of tree from preorder and inorder traversals

def construct_tree(inorder, preorder,inS,inE,prS,prE):
    if(inS>inE or prS>prE):
        return None
    root_data = preorder[prS]
    root = BinaryTreeNode(root)

    rootIndexInInorder = -1
    inorder.index()
    for i in range(inS,inE+1):
        if(inorder[i] == root_data):
            rootIndexInInorder = i
            break
    if(rootIndexInInorder == -1):
        print("Root not found")
        return None
    
    linS = inS
    linE = rootIndexInInorder-1
    lprS = prS+1
    lprE = linE + (linS - lprS)

    rinE = inE
    rprS= lprE+1
    rprE = prE
    # rprE - rprS = rinE - rinS
    rinS = rootIndexInInorder +1

    root.left = construct_tree(inorder, preorder,linS, linE, lprS, lprE)
    root.right = construct_tree(inorder, preorder, rinS, rinE, rprS, rprE)
    return root

