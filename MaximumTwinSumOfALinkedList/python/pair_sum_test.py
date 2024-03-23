from Common.python.ListNode import ListNode
from MaximumTwinSumOfALinkedList.python.pair_sum import Solution

class TestPairSum:
    def test_tied(self):
        assert 6 == Solution().pair_sum(head=ListNode.create_linked_list([5,4,2,1]))

    def test_ends(self):
        assert 7 == Solution().pair_sum(head=ListNode.create_linked_list([4,2,2,3]))

    def test_short(self):
        assert 100001 == Solution().pair_sum(head=ListNode.create_linked_list([1,100000]))

    def test_middle(self):
        assert 1003 == Solution().pair_sum(head=ListNode.create_linked_list([1,2,3, 1000, 90, 100]))
