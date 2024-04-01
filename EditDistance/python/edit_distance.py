class Solution:
    def minDistance_2D_DP(self, word1: str, word2: str) -> int:
        # todo optimization: Convert from 2D to 1D DP by only keeping 2 last rows to work with, and rework index 0s
        dp = [list(range(len(word1) + 1)) for _ in range(len(word2) + 1)]
        for i, c2 in enumerate(word2):
            row = i + 1
            dp[row][0] = row
            for j, c1 in enumerate(word1):
                col = j + 1
                if c1 == c2:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # 1 step from best of insert, delete or replace:
                    dp[row][col] = 1 + min(
                        dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]
                    )
        # for line in dp:
        #     print(line)
        return dp[-1][-1]

    def minDistance_1D_DP(self, word1: str, word2: str) -> int:
        # make word1 the smaller word by swapping
        if len(word2) < len(word1):
            word1, word2 = word2, word1
        # O(n) space, not n * n: Convert from 2D to 1D DP by only modulating between 2 last rows to work with
        dp = [[i for i in range(len(word1) + 1)] for _ in range(2)]
        row = 0
        for i, c2 in enumerate(word2):
            row = (i + 1) % 2
            dp[row][0] = dp[row - 1][0] + 1
            for j, c1 in enumerate(word1):
                col = j + 1
                if c1 == c2:
                    # ignore last char
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # 1 step from best of insert, delete or replace:
                    dp[row][col] = 1 + min(
                        dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]
                    )
            # print(dp[row])
        return dp[row][-1]
