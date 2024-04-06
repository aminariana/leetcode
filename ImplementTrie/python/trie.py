from collections import defaultdict


class Trie:

    def __init__(self):
        # self.val: str = None
        self.is_word = False
        self.children = defaultdict(str)

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trie()
            current = current.children[c]
        current.is_word = True
        # print(self)

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c not in current.children:
                return False
            else:
                current = current.children[c]
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c not in current.children:
                return False
            else:
                current = current.children[c]
        return True

    # def __str__(self, depth=0) -> str:
    #     result = ""
    #     for key in self.children:
    #         result += "\t" * depth + key + ("." if self.children[key].is_word else "")
    #         result += "\n" + self.children[key].__str__(depth + 1)
    #     return result


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
