'''
Day 13 - 30 days Leetcoding Challenge - April 13, 2020

Problem (leetcode-525)

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, d, maximum = 0, {0:0}, 0
        for i,v in enumerate(nums):
            count += 2*v -1
            if count in d:
                maximum = max(maximum,i+1-d[count])
            else:
                d[count] = i+1                
        return maximum 