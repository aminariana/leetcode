package MaxNumberOfKSumPairs.java;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxOperations(int[] nums, int k) {
        int result = 0;
        Map<Integer, Integer> complements = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (complements.containsKey(k - num)) {
                result++;
                int count = complements.getOrDefault(k - num, 0) - 1;
                if (count == 0)
                    complements.remove(k - num);
                else
                    complements.put(k - num, count);
            } else {
                complements.put(num, complements.getOrDefault(num, 0) + 1);
            }
        }
        return result;
    }
 }
  