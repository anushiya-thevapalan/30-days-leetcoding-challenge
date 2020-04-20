'''
Day 20 - 30 days Leetcoding Challenge - April 20, 2020

Problem (leetcode: 1008)

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:  
        root = TreeNode(preorder[0])
        stack = [root]

        for i in preorder[1:]:
            if i < stack[-1].val:
                node = TreeNode(i)
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < i:
                    pop = stack.pop()
                node = TreeNode(i)
                pop.right = node
                stack.append(node)
        return root