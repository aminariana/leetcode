package CanPlaceFlowers.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
  @Test
  void canPlaceOneInMiddle() {
    assertEquals(true, Solution.canPlaceFlowers(new int[] { 1, 0, 0, 0, 1 }, 1));
  }

  @Test
  void cannotPlaceTwoInMiddle() {
    assertEquals(false, Solution.canPlaceFlowers(new int[] { 1, 0, 0, 0, 1 }, 2));
  }
}
