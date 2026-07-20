"""
Problem: Two Sum (Easy)
Approach: hash map, one pass
Time: O(n) Space: O(n)
Edge cases: duplicates, negatives, empty(if allowed)
Alternatives: brute force(n^2), sorted two-pointers o(nlogn) if indices not needed
"""

from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen : dict[int, int] = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        raise ValueError("No two-sum solution") 

