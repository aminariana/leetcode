import pytest
from DeleteTheMiddleNodeOfALinkedList.python.delete_middle import deleteMiddle
from Common.python.ListNode import ListNode

class TestDeleteMiddle:
    def test_delete_odd(self):
        assert [1,3,4,1,2,6] == deleteMiddle(ListNode.create_linked_list([1,3,4,7,1,2,6])).to_list()

    def test_delete_even(self):
        assert [1,2,4] == deleteMiddle(ListNode.create_linked_list([1,2,3,4])).to_list()

    def test_delete_last(self):
        assert [2] == deleteMiddle(ListNode.create_linked_list([2,1])).to_list()
