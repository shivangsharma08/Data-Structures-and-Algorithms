# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    
    temp = llist
    if position == 0:
        return temp.next

    while position - 1 > 0:
        llist = llist.next
        position -= 1
    llist.next = llist.next.next
    return temp
    
