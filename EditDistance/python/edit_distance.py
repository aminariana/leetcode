class Solution:
   def minDistance_2D_DP(self, word1: str, word2: str) -> int:
       # optimization: Convert from 2D to 1D DP by only keeping 2 last rows to work with, and rework index 0s
       dp = [[0] * (len(word1)+1) for i in range(len(word2)+1)]
       for col in range(len(word1)+1):
           dp[0][col] = col
       for row in range(len(word2)+1):
           dp[row][0] = row
       for i, c2 in enumerate(word2):
           for j, c1 in enumerate(word1):
               row, col = i + 1, j + 1
               if c1 == c2:
                   dp[row][col] = dp[row - 1][col - 1]
               else:
                   if row == 0 and col == 0:
                       dp[row][col] = 1
                   elif col == 0:
                       dp[row][col] = dp[row-1][col] + 1
                   elif row == 0:
                       dp[row][col] = dp[row][col-1] + 1
                   else:
                       insert_cost = dp[row][col - 1] if col > 0 else row
                       delete_cost = dp[row - 1][col] if row > 0 else col
                       replace_cost = dp[row - 1][col - 1]
                       dp[row][col] = min(insert_cost, delete_cost, replace_cost) + 1
       for line in dp:
           print(line)
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
                   dp[row][col] = 1 + min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])
           # print(dp[row])
       return dp[row][-1]
