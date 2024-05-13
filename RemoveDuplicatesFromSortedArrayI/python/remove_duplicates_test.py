from RemoveDuplicatesFromSortedArrayI.python.remove_duplicates import removeDuplicates

class TestRemoveDuplicates:
    def test_one_dup(self):
        input = [1,1,2]
        output = removeDuplicates(input)
        assert input[:output] == [1, 2]

    def test_many_dups(self):
        input = [0,0,1,1,1,2,2,3,3,4]
        output = removeDuplicates(input)
        assert input[:output] == [0, 1, 2, 3, 4]
