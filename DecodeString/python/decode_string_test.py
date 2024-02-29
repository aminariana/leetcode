from DecodeString.python.decode_string import decodeString

class TestDecodeString:
    def test_basic_character(self):
        assert "a" == decodeString("a")

    def test_one_level_decode(self):
        assert "aaabcbc" == decodeString("3[a]2[bc]")

    def test_nested_decode(self):
        assert "accaccacc" == decodeString("3[a2[c]]")

    def test_substring_repeat(self):
        assert "abcabccdcdcdef" == decodeString("2[abc]3[cd]ef")

    def test_two_digit_repeat(self):
        assert "aaaaaaaaaa" == decodeString("10[a]")

    def test_two_digit_repeat_of_two_digit_repeat(self):
        assert "baaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaa" == decodeString("20[b10[a]]")

    def test_max_repeat(self):
        assert "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc" == decodeString("300[abc]")
