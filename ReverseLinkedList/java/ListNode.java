package ReverseLinkedList.java;

import java.util.List;

// Definition for singly-linked list.
public class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  ListNode(List<Integer> list) {
    this(list.size() > 0 ? list.get(0) : -1, list.size() > 1 ? new ListNode(list.subList(1, list.size())) : null);
  }

  @Override
  public String toString() {
    return "" + val + (next == null ? "" : "," + next.toString());
  }
}
