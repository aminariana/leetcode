package LongestConsecutiveSequence.java;

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static Map<Integer, Integer> memo = new HashMap<>();

    public static int longestConsecutive(int[] nums) {
        int ret = 0;
        for(int num : nums) memo.put(num, 0);
        for(int num : nums) ret = Math.max(ret, dfs(num));
        return ret;
    }
    
    private static int dfs(int v) {
        if (!memo.containsKey(v)) return 0;
        if (memo.get(v) == 0) memo.put(v, 1 + dfs(v + 1));
        return memo.get(v);
    }
}