from KeysAndRooms.python.can_visit_all_rooms import canVisitAllRooms

class TestKeysAndRooms:
    def test_positive(self):
        assert canVisitAllRooms([[1],[2],[3],[]])

    def test_negative(self):
        assert not canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
