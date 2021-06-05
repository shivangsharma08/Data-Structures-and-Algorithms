class Solution:
    def rightSideView(root):
        ar = []
        if (not root):
            return
        q = []
        q.append(root)
        while (len(q)):

            n = len(q)
            for i in range(1, n + 1):
                temp = q[0]
                q.pop(0)

                if (i == n):
                    ar.append(temp.val)

                if (temp.left != None):
                    q.append(temp.left)
                if (temp.right != None):
                    q.append(temp.right)
        return ar
