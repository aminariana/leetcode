from typing import Optional
from Common.python.ListNode import ListNode

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow, slow_prev = head, head, None
    while fast and fast.next:
        fast = fast.next.next
        slow_prev, slow = slow, slow.next
    # delete slow
    if slow_prev:
        slow_prev.next = slow.next
    return head.next if slow == head else head
