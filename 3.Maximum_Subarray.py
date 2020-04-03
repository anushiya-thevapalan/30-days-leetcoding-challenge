# Day 3 - 30 days Leetcoding Challenge - April 03, 2020

# Problem (leetcode-53)

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0: return None
        if length ==1: return nums[0]
        
        global_highest_sum = nums[0]
        local_highest_sum = nums[0]
        
        for i in range(1, length):
            total = local_highest_sum + nums[i]
            if  total >= nums[i]:
                local_highest_sum = total
            else:
                local_highest_sum = nums[i]
            if local_highest_sum > global_highest_sum:
                global_highest_sum = local_highest_sum
        return global_highest_sum
                
        
                
        
        