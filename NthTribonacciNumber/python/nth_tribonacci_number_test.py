import pytest
from NthTribonacciNumber.python import nth_tribonacci_number

class TestTribonacci:
    def test_four(self):
        assert 4 == nth_tribonacci_number.tribonacci(4)

    def test_zero(self):
        assert 0 == nth_tribonacci_number.tribonacci(0)

    def test_twenty_four(self):
        assert 755476 == nth_tribonacci_number.tribonacci(24)

    def test_thirty_seven(self):
        assert 2082876103 == nth_tribonacci_number.tribonacci(37)
