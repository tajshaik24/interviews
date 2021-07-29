'''
LeetCode 49. Group Anagrams

Given an array of strings, group anagrams together.
'''
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = defaultdict(list)
        for char in strs:
            key=''.join(sorted(char))
            memo[key].append(char)
        return list(memo.values())
