package IsSubsequence.java;

public class Solution {
    public boolean isSubsequence(String s, String t) {
        int j = 0; // s index
        for (int i = 0; i < t.length(); i++) { // t index
            if (j == s.length()) {
                return true; // everything in s matched
            }
            if (t.charAt(i) == s.charAt(j)) {
                j++;
            }
        }
        return j == s.length();
    }
 }
 