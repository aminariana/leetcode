package IncreasingTripletsSubsequence.java;

public class Solution {
    public boolean increasingTriplet(int[] nums) {
        int i = -1, j = -1;
        for (int k = 0; k < nums.length; k++) {
            if (i < 0 || nums[k] <= nums[i]) { // max < min ?
                i = k;
            } else if (j < 0 || nums[k] <= nums[j]) { // max < mid ?
                j = k;
            } else {
                return true;
            }
        }
        return false;
    }
}
