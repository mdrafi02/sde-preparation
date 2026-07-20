"""
Problem: isAnagram (Easy)
Approach: Counter
Time: O(n) Space: O(n)
Edge Cases: 
Alternatives:

"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

