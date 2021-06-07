# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    prev = None
    current = llist
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    llist = prev
    temp = llist
    while(temp):
        print(temp.data)
        temp = temp.next
