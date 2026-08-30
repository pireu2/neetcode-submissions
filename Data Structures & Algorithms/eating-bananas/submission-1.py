from functools import reduce
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        output = 0

        while left <= right:
            mid = (left + right) // 2

            time = sum(ceil(p / mid) for p in piles)

            if time <= h:
                output = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return output