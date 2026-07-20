"""
Given an array of integers 'num's and integer target, return indices of the two numbers such that they add up to 'target'.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:

    def two_sum(self, nums, target):
        my_dict = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return (i,my_dict[complement])
            my_dict[nums[i]] = i

