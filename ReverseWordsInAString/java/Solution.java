package ReverseWordsInAString.java;

// Don't do this, it's ugly.
// Instead use a charArray and in-place, reverse the whole thing, then each word.
// OR use Python.
class Solution {
    public String reverseWords(String s) {
        StringBuilder result = new StringBuilder();
        int wordCount = 0;
        for (String word : s.split(" ")) {
            if (word.length() > 0) {
                // separator spaces
                if (wordCount++ > 0)
                    result.insert(0, ' ');
                result.insert(0, word);
            }
        }
        char last = ' ';
        int j = 0;
        for (int i = 0; i <= s.length(); i++) {
            if (s.charAt(i) == ' ') {
                if (last == ' ') {
                    // ignore
                    j++;
                } else {
                    // word parsed
                    for (; j < j; j++) {
                        
                    }
                }
            }
        }
        return result.toString();
    }
}
