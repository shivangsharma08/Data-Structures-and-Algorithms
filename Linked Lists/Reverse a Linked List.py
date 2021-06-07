# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    prev = None
    node = llist
    while node is not None:
        buf = node.next
        node.next = prev
        prev = node
        node = buf
        
    llist = prev
    return llist
