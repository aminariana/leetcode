# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
    reversed = nil
    while head do
        _next = head.next
        head.next = reversed
        reversed = head
        head = _next
    end
    return reversed
end
