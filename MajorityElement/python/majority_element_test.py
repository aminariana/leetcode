from MajorityElement.python.majority_element import majorityElement

class TestMajorityElement:
    def test_tie_breaker(self):
        assert 3 == majorityElement([3,2,3])

    def test_resilient(self):
        assert 2 == majorityElement([2,2,1,1,1,2,2])

    def test_long(self):
        assert 4 == majorityElement([4, 4, 1, 2, 4])

    def test_late_candidate(self):
        assert 4 == majorityElement([1, 4, 4, 2, 4])

    def test_drama(self):
        assert 4 == majorityElement([1,4,4,4,2,1,4,4,2])
