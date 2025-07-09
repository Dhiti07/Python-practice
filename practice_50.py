# diameter of a tree

def diameter_of_a_tree(root):
    if(root is None):
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    left_diameter = diameter_of_a_tree(root.left)
    right_diameter = diameter_of_a_tree(root.right)

    ans = max(left_diameter,right_diameter,leftHeight+rightHeight)
    return ans