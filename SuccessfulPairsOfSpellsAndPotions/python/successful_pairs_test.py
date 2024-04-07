from SuccessfulPairsOfSpellsAndPotions.python.successful_pairs import successfulPairs

class TestSuccessfulPairs:
    def test_sorted(self):
        assert [4,0,3] == successfulPairs(spells=[5,1,3], potions=[1,2,3,4,5], success=7)

    def test_unsorted(self):
        assert [2,0,2] == successfulPairs(spells=[3,1,2], potions=[8,5,8], success=16)
