package SumDivisibles.java;

import static SumDivisibles.java.Solution.SumNaturalNumbers;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.List;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    void testSumsNaturalNumbersLTE10() {
        assertEquals(55, SumNaturalNumbers(10));
    }

    @Test
    void testSumsNaturalNumbersLTE97() {
        assertEquals(4753, SumNaturalNumbers(97));
    }

    @Test
    void testSumsNaturalNumbersThatAreMultiplesOf3AndLTE12() {
        assertEquals(30, SumNaturalNumbers(12, 3));
    }

    @Test
    void testSumsNaturalNumbersThatAreMultiplesOf3Or5AndLTE15() {
        assertEquals(60, SumNaturalNumbers(15, List.of(3, 5)));
    }

    @Test
    void testSumsNaturalNumbersThatAreMultiplesOf3Or5Or7Or44AndLTE1000() {
        assertEquals(277038, SumNaturalNumbers(1000, List.of(3, 5, 7, 44)));
    }
}
