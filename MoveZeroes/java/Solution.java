package MoveZeroes.java;

class Solution {
    public void moveZeroes(int[] nums) {
        int j = -1; // insertion index
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0 && j < 0)
                j = i;
            if (nums[i] != 0 && j > -1) {
                nums[j++] = nums[i];
                nums[i] = 0;
            }
        }
    }
 }
 