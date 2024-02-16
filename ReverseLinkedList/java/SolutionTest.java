package ReverseLinkedList.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void empty() {
        List<Integer> list = Arrays.asList();
        ListNode listNode = new ListNode(list);
        assertEquals("[]", list.toString());
        assertEquals("-1", listNode.toString());
        assertEquals("-1", Solution.reverseList(listNode).toString());
    }

    @Test
    void single() {
        List<Integer> list = Arrays.asList(1);
        ListNode listNode = new ListNode(list);
        assertEquals("[1]", list.toString());
        assertEquals("1", listNode.toString());
        assertEquals("1", Solution.reverseList(listNode).toString());
    }

    @Test
    void two() {
        List<Integer> list = Arrays.asList(1,2);
        ListNode listNode = new ListNode(list);
        assertEquals("[1, 2]", list.toString());
        assertEquals("1,2", listNode.toString());
        assertEquals("2,1", Solution.reverseList(listNode).toString());
    }

    @Test
    void many() {
        List<Integer> list = Arrays.asList(1,2,3,4,5);
        ListNode listNode = new ListNode(list);
        assertEquals("[1, 2, 3, 4, 5]", list.toString());
        assertEquals("1,2,3,4,5", listNode.toString());
        assertEquals("5,4,3,2,1", Solution.reverseList(listNode).toString());
    }
}