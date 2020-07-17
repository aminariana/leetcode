package CountOfNumbersAfterSelf;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> counts = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>();
        for(int i = nums.length - 1; i >= 0; i--) {
            int j = Collections.binarySearch(sorted, nums[i]);
            if (j < 0) j = -j-1; // insert position if new
            else while(j > 0 && sorted.get(j-1) == nums[i]) j--; // first index of dups
            sorted.add(j, nums[i]);
            counts.add(0, j);
        }
        return counts;
    }
}
