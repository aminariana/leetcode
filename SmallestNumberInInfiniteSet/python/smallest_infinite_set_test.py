from Common.python.assert_calls import assert_calls
from SmallestNumberInInfiniteSet.python.smallest_infinite_set import SmallestInfiniteSet

class TestSmallestInfiniteSet:
    def test_push_again(self):
        assert_calls(
            SmallestInfiniteSet(),
            ["addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"],
            [[2],[],[],[],[1],[],[],[]],
            [None,1,2,3,None,1,4,5]
        )

    def test_push_duplicates(self):
        assert_calls(
            SmallestInfiniteSet(),
            ["popSmallest", "popSmallest", "addBack", "addBack", "popSmallest","popSmallest"],
            [[],[],[1],[1],[],[]],
            [1,2,None,None,1,3]
        )
