from RemoveDuplicatesFromSortedArrayII.python.remove_duplicates2 import removeDuplicates

class TestRemoveDuplicates2:
    def test_one_dudup(self):
        input = [1,1,1,2,2,3]
        output = removeDuplicates(input)
        assert input[:output] == [1, 1, 2, 2, 3]

    def test_many_dudups(self):
        input = [0,0,1,1,1,1,2,3,3]
        output = removeDuplicates(input)
        assert input[:output] == [0, 0, 1, 1, 2, 3, 3]
