package FindPivotIndex.java;

class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        int prefix = 0;
        for (int i = 0; i < nums.length; i++) { // pivot
            if (i > 0) {
                prefix += nums[i - 1];
            }
            if  (prefix * 2 + nums[i] == sum) {
                return i;
            }
        }
        return -1;
    }
}
