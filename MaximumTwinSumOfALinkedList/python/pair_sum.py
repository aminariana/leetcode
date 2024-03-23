from typing import Optional

from Common.python.ListNode import ListNode


class Solution:
    def pair_sum(self, head: Optional[ListNode]) -> int:
        mid = self.find_mid(head)
        rev = self.reverse_list(mid)
        pair_max = 0
        while head and rev:
            pair = head.val + rev.val
            pair_max = max(pair_max, pair)
            head = head.next
            rev = rev.next
        return pair_max

    def find_mid(self, head: Optional[ListNode]):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: Optional[ListNode]):
        rev = None
        while head:
            rest = head.next
            head.next = rev
            rev = head
            head = rest
        return rev
