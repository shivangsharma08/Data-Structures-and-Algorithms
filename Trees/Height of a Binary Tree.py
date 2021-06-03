'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    
    if(root != None):
        return(max(1 + height(root.left), 1+ height(root.right)))
    else:
        return(-1)
