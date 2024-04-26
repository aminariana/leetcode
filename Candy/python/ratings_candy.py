from collections import defaultdict
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            else:
                candies[i] = 1

        for i in reversed(range(len(ratings))):
            if i < len(ratings)-1 and ratings[i] > ratings[i+1]:
                if candies[i+1] + 1 > candies[i]:
                    candies[i] = candies[i+1] + 1

        # print(candies)
        return sum(candies)

    def candy_dfs(self, ratings: List[int]) -> int:
        index_by_rating = defaultdict(int)
        for i, rating in enumerate(ratings):
            if rating not in index_by_rating:
                index_by_rating[rating] = []
            index_by_rating[rating].append(i)
        # print(dict(index_by_rating))
        rate_stack = list(reversed(sorted(index_by_rating.keys())))
        # print(rate_stack)

        candies = [0] * len(ratings)

        def dfs(i):
            # print(f"dfs index {i}")
            if candies[i] > 0:
                return
            candies[i] = 1
            for right in range(i+1, len(candies)):
                if ratings[right] > ratings[right-1] and candies[right] <= candies[right-1]:
                    candies[right] = candies[right-1] + 1
                    # print(f"candies[{right}] = {candies[right]}")
                else:
                    break
            for left in reversed(range(0, i)):
                if ratings[left] > ratings[left+1] and candies[left] <= candies[left+1]:
                    candies[left] = candies[left+1] + 1
                    # print(f"candies[{left}] = {candies[left]}")
                else:
                    break
        while len(rate_stack):
            rate = rate_stack.pop()
            for i in index_by_rating[rate]:
                dfs(i)
        # print(candies)
        return sum(candies)
