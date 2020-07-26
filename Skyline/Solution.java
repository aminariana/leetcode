package Skyline;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> sky = new ArrayList<>();
        List<List<Integer>> bars = new ArrayList<>();
        PriorityQueue<Integer> roofs = new PriorityQueue<>((h1, h2) -> h2 - h1);

        for (int[] b : buildings) {
            bars.add(Arrays.asList(b[0], b[2]));
            bars.add(Arrays.asList(b[1], -b[2])); // negative means right of building
        }
        Collections.sort(bars, (b1, b2) -> // for dup x, higher bar first
            b1.get(0) == b2.get(0) ? b2.get(1) - b1.get(1) : b1.get(0) - b2.get(0));
        List<Integer> prev = null;
        for(List<Integer> bar : bars) {
            int x = bar.get(0), hi = bar.get(1), skyline = prev == null ? 0 : prev.get(1);
            if (hi < 0) { // right of building
                roofs.remove(-hi);
                int drop = roofs.isEmpty() ? 0 : roofs.peek();
                if (drop == skyline) continue;
                if (x == prev.get(0) && drop < skyline) prev.set(1, drop);// same right? lowest rooftop.
                else sky.add(prev = Arrays.asList(x, drop)); // else drop to next rooftop
            } else { // left of building
                roofs.add(hi);
                if (hi > skyline) sky.add(prev = bar);
            }
        }
        return sky;
    }
}
