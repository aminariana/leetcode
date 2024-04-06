from ImplementTrie.python.trie import Trie

class TestTrie:
    def test_trie(self):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple")
        assert not trie.search("app")
        assert trie.startsWith("app")
        trie.insert("app")
        assert trie.search("app")
