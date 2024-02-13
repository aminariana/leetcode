package KidsWithCandies.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void multipleCandidates() {
        assertEquals("[true, true, true, false, true]",
            Solution.kidsWithCandies(new int[] { 2,3,5,1,3 }, 3).toString());
    }

    @Test
    void multipleRejects() {
        assertEquals("[true, false, false, false, false]",
            Solution.kidsWithCandies(new int[] { 4,2,1,1,2 }, 1).toString());
    }

    @Test
    void localSubOptima() {
        assertEquals("[true, false, true]",
            Solution.kidsWithCandies(new int[] { 12,1,12 }, 10).toString());
    }
}
