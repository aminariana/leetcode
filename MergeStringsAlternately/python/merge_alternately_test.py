from MergeStringsAlternately.python.merge_alternately import mergeAlternately

class TestMergeAlternately:
    def test_equal_length(self):
        assert "apbqcr" == mergeAlternately("abc", "pqr")

    def test_right_longer(self):
        assert "apbqrs" == mergeAlternately("ab", "pqrs")

    def test_left_longer(self):
        assert "apbqcd" == mergeAlternately("abcd", "pq")
