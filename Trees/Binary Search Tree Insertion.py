#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        
        current = self.root
        while True:
            if current.info > val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            else:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
    
        return self.root