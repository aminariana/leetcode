from RemoveElement.python.remove_element import removeElement

class TestRemoveElement:
    def test_twice(self):
        array = [3,2,2,3]
        remain = removeElement(array, 3)
        assert 2 == remain
        assert sorted(array[:remain]) == sorted([2,2])

    def test_disconnected(self):
        array = [0,1,2,2,3,0,4,2]
        remain = removeElement(array, 2)
        assert 5 == remain
        assert sorted(array[:remain]) == sorted([0,1,4,0,3])