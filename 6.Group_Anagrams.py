'''
Day 6 - 30 days Leetcoding Challenge - April 06, 2020

Problem (leetcode-49)
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from collections import defaultdict
class Solution:
    '''
    Approach 1: Time complexity: O(N.K.logK), Space complexity: O(N.K)
    N iterations and K log(K) for sorting
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            anagrams[tuple(sorted(i))].append(i)
        return anagrams.values()

    '''
    Approach 2: Time complexity: O(N.K), Space complexity: O(N.K)
    '''
    def groupAnagrams_approach2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()