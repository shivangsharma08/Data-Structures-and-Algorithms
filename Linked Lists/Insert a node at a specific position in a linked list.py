# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):

    new = SinglyLinkedListNode(data)
   
    pointer = llist
    counter = 1
    while pointer.next is not None:
        if counter == position:
            new.next = pointer.next
            pointer.next = new
            break
        counter += 1
        pointer = pointer.next
    return llist
