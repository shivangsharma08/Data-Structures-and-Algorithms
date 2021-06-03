def preOrder(root):

    if(root!= None):
        print(root,end=" ")
        preOrder(root.left)
        preOrder(root.right)