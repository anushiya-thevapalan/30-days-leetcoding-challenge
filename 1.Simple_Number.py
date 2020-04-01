# Day 1 - 30 days Leetcoding Challenge - April 01, 2020

# Problem (leetcode-136)

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    # Approach 1
    def singleNumber_approach_1(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    # Approach 2
    def singleNumber_approach_2(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = i ^ nums
        return result