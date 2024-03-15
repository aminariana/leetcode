from LetterCombinationsOfAPhoneNumber.python.letter_combinations import letterCombinations

class TestLetterCombinations:
    def test_two_digits(self):
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert expected == letterCombinations("23")

    def test_empty(self):
        expected = []
        assert expected == letterCombinations("")

    def test_single(self):
        expected = ["a","b","c"]
        assert expected == letterCombinations("2")

    def test_four_digits(self):
        expected = ["adpm","adpn","adpo","adqm","adqn","adqo","adrm","adrn","adro","adsm","adsn","adso","aepm","aepn","aepo","aeqm","aeqn","aeqo","aerm","aern","aero","aesm","aesn","aeso","afpm","afpn","afpo","afqm","afqn","afqo","afrm","afrn","afro","afsm","afsn","afso","bdpm","bdpn","bdpo","bdqm","bdqn","bdqo","bdrm","bdrn","bdro","bdsm","bdsn","bdso","bepm","bepn","bepo","beqm","beqn","beqo","berm","bern","bero","besm","besn","beso","bfpm","bfpn","bfpo","bfqm","bfqn","bfqo","bfrm","bfrn","bfro","bfsm","bfsn","bfso","cdpm","cdpn","cdpo","cdqm","cdqn","cdqo","cdrm","cdrn","cdro","cdsm","cdsn","cdso","cepm","cepn","cepo","ceqm","ceqn","ceqo","cerm","cern","cero","cesm","cesn","ceso","cfpm","cfpn","cfpo","cfqm","cfqn","cfqo","cfrm","cfrn","cfro","cfsm","cfsn","cfso"]
        assert expected == letterCombinations("2376")
