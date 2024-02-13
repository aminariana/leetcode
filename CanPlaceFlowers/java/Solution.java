package CanPlaceFlowers.java;

public class Solution {
  public static boolean canPlaceFlowers(int[] flowerbed, int n) {
    int result = 0;
    for (int i = 0; i < flowerbed.length; i++) {
      if (flowerbed[i] == 0) {
        if ((i == 0 || flowerbed[i - 1] == 0) &&
            (i + 1 == flowerbed.length || flowerbed[i + 1] == 0)) { // start or clear
          flowerbed[i] = 1; // plant!
          result++;
        }
      }
    }
    return result >= n;
  }
}
