from RemovingStarsFromAString.python.remove_stars import removeStars

class TestRemoveStars:
    def test_some_removes(self):
        assert "lecoe" == removeStars("leet**cod*e")

    def test_all_removes(self):
        assert "" == removeStars("erase*****")
