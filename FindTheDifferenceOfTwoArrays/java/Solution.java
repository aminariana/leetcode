package FindTheDifferenceOfTwoArrays.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Solution {
    // Deliberately avoided a HashMap here, YMMV.
    public List<List<Integer>> findDifference1(int[] nums1, int[] nums2) {
        boolean[] bitmap1 = new boolean[2001]; // bitmap of values
        boolean[] bitmap2 = new boolean[2001]; // bitmap of values
        // nums[i] is between -1000 and 1000
        for (int i = 0; i < nums1.length; i++) {
            bitmap1[nums1[i] + 1000] = true;
        }
        for (int i = 0; i < nums2.length; i++) {
            bitmap2[nums2[i] + 1000] = true;
        }
        List<Integer> diff1 = new LinkedList<>();
        List<Integer> diff2 = new LinkedList<>();
        for (int i = 0; i < bitmap1.length; i++) { // for each value
            if (bitmap1[i] && !bitmap2[i]) {
                diff1.add(i - 1000);
            }
            if (!bitmap1[i] && bitmap2[i]) {
                diff2.add(i - 1000);
            }
        }
        return Arrays.asList(diff1, diff2);
    }

    // Lower performance but more readable
    public List<List<Integer>> findDifference2(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>(Arrays.stream(nums1).boxed().collect(Collectors.toList()));
        Set<Integer> set2 = new HashSet<>(Arrays.stream(nums2).boxed().collect(Collectors.toList()));
        Set<Integer> diff1 = Set.copyOf(set1);
        diff1.removeAll(set2);
        Set<Integer> diff2 = Set.copyOf(set2);
        diff1.removeAll(set1);
        return Arrays.asList(new ArrayList<Integer>(diff1), new ArrayList<Integer>(diff2));
    }
}