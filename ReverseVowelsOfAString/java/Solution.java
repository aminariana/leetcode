package ReverseVowelsOfAString.java;

class Solution {
    public String reverseVowels(String s) {
        char[] charArray = s.toCharArray();
        int j = s.length() - 1;
        for (int i = 0; i < j; ) {
            if (isVowel(charArray[i])) {
                if (isVowel(charArray[j])) {
                    // swap
                    char c = charArray[i];
                    charArray[i] = charArray[j];
                    charArray[j] = c;
                    i++;
                }
                j--;
            } else { // i not vowel
                if (!isVowel(charArray[j])) {
                    j--;
                }
                i++;
            }
        }
        return new String(charArray);
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
