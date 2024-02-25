from typing import Optional
from Common.python.ListNode import ListNode

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    # deal with no head to simplify the rest of code
    if not head: return head
    even_head = head.next
    odd, even = head, even_head

    # while an odd node hasn't been seen
    while even and even.next:
        # link the unseen odd node to odd list
        odd.next = even.next
        odd = odd.next

        # unlink said odd node from the even list
        even.next = odd.next
        even = even.next

    # connect the two lists
    odd.next = even_head
    return head
