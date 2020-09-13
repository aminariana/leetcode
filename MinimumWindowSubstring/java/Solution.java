package MinimumWindowSubstring.java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String minWindow(String s, String t) {
        if (s == null || t == null) return null;
        Map<Character, Integer> histogram = new HashMap<>(), set = new HashMap<>(), unmatched = new HashMap<>();
        Deque<Integer> window = new ArrayDeque<>();
        int left = 0, right = 0, min = Integer.MAX_VALUE;
        for(char c : t.toCharArray()) {
            int freq = set.getOrDefault(c, 0) + 1;
            set.put(c, freq);
            unmatched.put(c, freq);
        }
        // System.out.println("t: " + set);
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!set.containsKey(c)) continue;
            window.addLast(i);
            histogram.put(c, histogram.getOrDefault(c, 0) + 1);
            if (unmatched.containsKey(c))
                if (unmatched.get(c) == 1) unmatched.remove(c);
                else unmatched.put(c, unmatched.get(c) - 1);
            while(histogram.get(s.charAt(window.peekFirst())) > set.get(s.charAt(window.peekFirst()))) {
                char head = s.charAt(window.removeFirst());
                histogram.put(head, histogram.get(head) - 1);
            }
            int size = window.peekLast() - window.peekFirst() + 1;
            if (unmatched.isEmpty() && size < min) {
                min = size;
                left = window.peekFirst();
                right = window.peekLast() + 1;
            }
            // System.out.println(window + " " + c + " " + histogram);
        }
        return s.substring(left, right);
    }
}