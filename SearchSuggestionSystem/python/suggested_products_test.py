from SearchSuggestionSystem.python.suggested_products import Solution


class TestSearchSuggestionSystem:
    def test_dictionary(self):
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ]
        assert expected == Solution().suggestedProducts(
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
        )

    def test_single_match(self):
        expected = [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ]
        assert expected == Solution().suggestedProducts(["havana"], "havana")

    def test_single_non_match(self):
        expected = [[], [], [], [], [], [], []]
        assert expected == Solution().suggestedProducts(["havana"], "tatiana")

    def test_broken_prefix(self):
        expected = [["foobar"], ["foobar"], [], []]
        assert expected == Solution().suggestedProducts(["foobar"], "foxo")
