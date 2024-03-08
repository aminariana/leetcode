package ProductOfArrayExceptSelf.java;

import java.util.Arrays;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);
        int prefix = 1;
        int suffix = 1;
        for (int i = 0; i < nums.length; i++) {
            int j = nums.length - i - 1;
            answer[i] *= prefix;
            answer[j] *= suffix;
            prefix *= nums[i];
            suffix *= nums[j];
        }
        return answer;
    }
}