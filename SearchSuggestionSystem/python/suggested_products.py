from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(str)
        self.word = None

    def insert(self, word: str):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trie()
            current = current.children[c]
        current.word = word

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        trie = Trie()
        for product in products:
            trie.insert(product)

        prefix = trie
        prefix_stopped = False
        for i, c in enumerate(searchWord):
            suggest = []
            if not prefix_stopped and c in prefix.children:
                prefix = prefix.children[c]
                stack = [prefix]
                while len(stack):
                    pop = stack.pop()
                    if pop.word:
                        suggest.append(pop.word)
                        if len(suggest) == 3: break
                    for key in reversed(sorted(pop.children.keys())):
                        stack.append(pop.children[key])
            else:
                prefix_stopped = True
            result.append(suggest)
        return result
