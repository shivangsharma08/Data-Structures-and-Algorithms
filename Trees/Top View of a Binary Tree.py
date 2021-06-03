def topView(root):
    if(root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
 
    while(len(q)):
        root = q[0]
        hd = root.hd
        if hd not in m:
            m[hd] = root
        if(root.left):
            root.left.hd = hd - 1
            q.append(root.left)
 
        if(root.right):
            root.right.hd = hd + 1
            q.append(root.right)
 
        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")