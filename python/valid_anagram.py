"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            my_dict = dict()
            for i in range(len(s)):
                if s[i] in my_dict:
                    my_dict[s[i]] += 1
                else:
                    my_dict[s[i]] = 1

            for i in range(len(t)):
                if t[i] in my_dict and my_dict[t[i]] > 0:
                    my_dict[t[i]] -= 1
                else:
                    return False

            for i in range(len(s)):
                if my_dict[s[i]] == 1:
                    return False
            return True
        return False

