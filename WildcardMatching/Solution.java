package WildcardMatching;

class Solution {
    public boolean isMatch(String s, String p) {
        int pLen = p.length(), sLen = s.length();
        boolean[][] dp = new boolean[pLen + 1][sLen + 1];
        dp[0][0] = true;
        for(int i = 1; i <= pLen; i++) dp[i][0] = dp[i-1][0] && p.charAt(i-1) == '*';
        for(int i = 1; i <= pLen; i++) {
            char pChar = p.charAt(i-1);
            for(int j = 1; j <= sLen; j++)
                switch(pChar) {
                    case '*': dp[i][j] = dp[i][j-1] || dp[i-1][j]; break;
                    case '?': dp[i][j] = dp[i-1][j-1]; break;
                    default:  dp[i][j] = dp[i-1][j-1] && s.charAt(j-1) == pChar;
                }
        }
        return dp[pLen][sLen];
    }
}