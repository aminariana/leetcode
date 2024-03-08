from GuessNumberHigherOrLower.python.guess_number import Guess

class TestGuess:
    def test_mid(self):
        guesser = Guess(6)
        assert 6 == guesser.guessNumber(10)
        
    def test_only(self):
        guesser = Guess(1)
        assert 1 == guesser.guessNumber(1)

    def test_low(self):
        guesser = Guess(1)
        assert 1 == guesser.guessNumber(2)