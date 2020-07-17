package SumDivisibles;

import java.util.List;

public class Solution {
    public int SumNaturalNumbers(int n) {
        return n * (n+1) / 2;
    }

    // e.g. 12, 3 -> 3 + 6 + 9 + 12 -> 3 * (1 + 2 + 3 + 4)
    public int SumNaturalNumbers(int n, int divider) {
        return divider * SumNaturalNumbers(n / divider);
    }
    
    public int SumNaturalNumbers(int n, List<Integer> dividers) {
        int ret = 0;
        boolean yes = false;
        for(int i = 1; i <= n; i++) {
            yes = false;
            for(int divider : dividers)
                if (i % divider == 0) yes = true;
            if (yes) ret += i;
        }
        return ret;
    }
}        
