package Common.java;

import java.util.List;

// Definition for singly-linked list.
public class ListNode {
  public int val;
  public ListNode next;
  public ListNode() {}
  public ListNode(int val) { this.val = val; }
  public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  public ListNode(List<Integer> list) {
    this(list.size() > 0 ? list.get(0) : -1, list.size() > 1 ? new ListNode(list.subList(1, list.size())) : null);
  }

  @Override
  public String toString() {
    return "" + val + (next == null ? "" : "," + next.toString());
  }
}
