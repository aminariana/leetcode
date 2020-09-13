package LongestConsecutiveSequence.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void empty() {
        assertEquals(0, Solution.longestConsecutive(new int[] { }));
    }

    @Test
    void unordered() {
        assertEquals(4, Solution.longestConsecutive(new int[] { 100, 4, 200, 1, 3, 2 }));
    }
}
