package SlidingWindowMaximum;

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    private class Pair {
        public int key, val;
        public Pair(int key, int val) { this.key = key; this.val = val; }
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] max = new int[nums.length - k + 1];
        Deque<Pair> window = new ArrayDeque<>();
        for(int i = 0; i < nums.length; i++) {
            int deleted = 0;
            while (!window.isEmpty() && window.peekLast().key < nums[i])
                deleted += 1 + window.removeLast().val;
            window.addLast(new Pair(nums[i], deleted));
            if (i + 1 >= k) {
                Pair head = window.peekFirst();
                max[i-k+1] = head.key;
                if (head.val > 0) head.val--;
                else window.removeFirst();
            }
        }
        return max;
    }
}