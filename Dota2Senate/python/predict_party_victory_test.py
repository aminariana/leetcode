from Dota2Senate.python.predict_party_victory import predictPartyVictory

class TestPredictPartyVictory:
    def test_two_opponents(self):
        assert "Radiant" == predictPartyVictory("RD")

    def test_majority(self):
        assert "Dire" == predictPartyVictory("RDD")
