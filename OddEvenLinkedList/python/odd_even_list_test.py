import pytest
from Common.python.ListNode import ListNode
from OddEvenLinkedList.python.odd_even_list import oddEvenList

class TestOddEvenLinkedList:
    def test_normal(self):
        head = ListNode.create_linked_list([1,2,3,4,5])
        assert [1,3,5,2,4] == oddEvenList(head).to_list()

    def test_random(self):
        head = ListNode.create_linked_list([2,1,3,5,6,4,7])
        assert [2,3,6,7,1,5,4] == oddEvenList(head).to_list()

    def test_small(self):
        head = ListNode.create_linked_list([1,2])
        assert [1,2] == oddEvenList(head).to_list()

    def test_small_reversed(self):
        head = ListNode.create_linked_list([2,1])
        assert [2,1] == oddEvenList(head).to_list()

    def test_ambiguous(self):
        head = ListNode.create_linked_list([2,2])
        assert [2,2] == oddEvenList(head).to_list()

    def test_badly_sorted(self):
        head = ListNode.create_linked_list([2,4,6,8,1,3,5])
        assert [2,6,1,5,4,8,3] == oddEvenList(head).to_list()

    def test_empty(self):
        head = ListNode.create_linked_list([])
        assert None == oddEvenList(head)
