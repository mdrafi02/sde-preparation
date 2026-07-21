"""
Problem: isPalindrome (Easy)
Approach: Two Pointers
Time: O(n) Space: O(1)
Edge Cases:
Alternatives:

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(result) - 1
        
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1

        return True


        
