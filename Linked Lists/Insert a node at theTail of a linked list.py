# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = head
    if head is None:
        head = SinglyLinkedListNode(data)
        return(head)
    
    while  node.next != None:
        node = node.next
    
    node.next = SinglyLinkedListNode(data)
    
    return(head)

