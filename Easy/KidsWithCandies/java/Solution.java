package Easy.KidsWithCandies.java;

import java.util.ArrayList;
import java.util.List;

public class Solution {
  public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
    // calculate max, then run again and compare to each e + x
    int max = 0;
    List<Boolean> results = new ArrayList<Boolean>();
    for (int i = 0; i < candies.length; i++) {
      max = Math.max(max, candies[i]);
    }
    for (int i = 0; i < candies.length; i++) {
      results.add(candies[i] + extraCandies >= max);
    }
    return results;
  }
}
