'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.
'''
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        def backTracking(pattern,S,D):
            if len(pattern) == 0 and len(S) == 0:
                return True
            if len(pattern) == 0:
                return False
            for i in range(1, len(S) - len(pattern) + 2):
                if pattern[0] not in D and S[:i] not in D.values():
                    D[pattern[0]] = S[:i]
                    if backTracking(pattern[1:], S[i:], D):
                        return True
                    del D[pattern[0]]
                elif pattern[0] in D and D[pattern[0]] == S[:i]:
                    if backTracking(pattern[1:], S[i:],D):
                        return True
            return False
        return backTracking(pattern,str,{})
