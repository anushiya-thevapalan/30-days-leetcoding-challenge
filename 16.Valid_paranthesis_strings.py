'''
Day 16 - 30 days Leetcoding Challenge - April 16, 2020

Problem (leetcode: 678)

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            elif x == '*':
                star.append(i)
            else:
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
        
        while stack and star:
            if stack.pop() > star.pop():
                return False
        
        if not stack:
            return True
        else:
            return False