from typing import List

class Solution:
   def maxOperations(self, nums: List[int], k: int) -> int:
       result = 0
       complements = {}
       for num in nums:
           if k - num in complements:
               result += 1
               complements[k - num] -= 1
               if complements[k - num] == 0:
                   del complements[k - num]
           else:
               complements[num] = complements.get(num, 0) + 1
       return result
