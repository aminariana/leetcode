package MinimumWindowSubstring.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void emptyStringAndPattern() {
        assertEquals("", Solution.minWindow("", ""));
    }

    @Test
    void emptyString() {
        assertEquals("", Solution.minWindow("", "pattern"));
    }

    @Test
    void emptyPattern() {
        assertEquals("", Solution.minWindow("string", ""));
    }

    @Test
    void nullString() {
        assertEquals(null, Solution.minWindow(null, "pattern"));
    }

    @Test
    void nullPattern() {
        assertEquals(null, Solution.minWindow("string", null));
    }

    @Test
    void matchPatternOnce() {
        assertEquals("", Solution.minWindow("a", "aa"));
    }

    @Test
    void normalMatch() {
        assertEquals("BANC", Solution.minWindow("ADOBECODEBANC", "ABC"));
    }

    @Test
    void pickShortestOfAmbiguousMatches() {
        assertEquals("baca", Solution.minWindow("acbbaca", "aba"));
    }
}
