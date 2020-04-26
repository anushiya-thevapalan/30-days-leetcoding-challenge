'''
Day 23 - 30 days Leetcoding Challenge - April 23, 2020

Problem (leetcode: 201)

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return 0 if  n >= m*2 else functools.reduce(lambda x, y: x & y, range(m, n+1))