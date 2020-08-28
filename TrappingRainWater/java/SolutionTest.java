package TrappingRainWater;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void empty() {
        assertEquals(0, Solution.trap(new int[] { }));
    }

    @Test
    void hill() {
        assertEquals(0, Solution.trap(new int[] { 0, 1, 2, 1, 0 }));
    }

    @Test
    void bowl() {
        assertEquals(4, Solution.trap(new int[] { 2, 1, 0, 1, 2 }));
    }

    @Test
    void normal() {
        assertEquals(6, Solution.trap(new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 }));
    }
}
