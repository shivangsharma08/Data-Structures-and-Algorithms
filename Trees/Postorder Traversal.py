def postOrder(root):
   if(root != None):
    postOrder(root.left)
    postOrder(root.right)
    print(root,end=" ")
