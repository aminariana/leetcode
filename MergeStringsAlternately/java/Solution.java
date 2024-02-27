package MergeStringsAlternately.java;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] result = new char[word1.length() + word2.length()];

        int j = 0;
        for (int i = 0; i < word1.length() || i < word2.length(); i++) {
            if (i < word1.length()) {
                result[j++] = word1.charAt(i);
            }
            if (i < word2.length()) {
                result[j++] = word2.charAt(i);
            }
        }
        return new String(result);
    }
}
