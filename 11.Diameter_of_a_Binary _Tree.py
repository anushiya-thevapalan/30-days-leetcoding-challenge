'''
Day 11 - 30 days Leetcoding Challenge - April 11, 2020

Problem (leetcode-543)

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:       
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.maximum = 1
        
        def recursion(node):
            if not node:
                return 0
            else:
                left = recursion(node.left)
                right = recursion(node.right)
                self.maximum = max(self.maximum, left+right+1)
                
                return max(left, right) + 1
        recursion(root)

        # subtract 1 as the diameter is the number of edges, NOT nodes        
        return self.maximum - 1