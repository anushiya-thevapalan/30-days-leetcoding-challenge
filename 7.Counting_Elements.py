'''
Day 7 - 30 days Leetcoding Challenge - April 07, 2020

Problem (leetcode-new problem)

Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
'''
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0
        for i in arr:
            if i+1 in arr_set:
                count+=1
        return count
                