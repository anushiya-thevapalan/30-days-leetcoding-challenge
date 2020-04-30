'''
Day 29 - 30 days Leetcoding Challenge - April 29, 2020

Problem (leetcode: 124)

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''
class Solution(object):
    def maxPathSum(self, root):
        self.max = float('-inf')
        def get_sum(root):
            if root is None:
                return 0
            else:
                ls = max(get_sum(root.left), 0)
                rs = max(get_sum(root.right), 0)
                self.max = max(self.max, ls + rs + root.val)
                return max(ls, rs, 0) + root.val
        
        get_sum(root)
        return self.max