def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root, end=" ")
        inOrder(root.right)