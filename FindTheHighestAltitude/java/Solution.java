class Solution {
    public int largestAltitude(int[] gain) {
        int alt = 0;
        int max = 0;
        for (int i = 0; i < gain.length; i++) {
            alt += gain[i];
            max = Math.max(max, alt);
        }
        return max;
    }
 }
