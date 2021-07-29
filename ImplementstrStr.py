'''
LeetCode 28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for index, char in enumerate(haystack):
            if char == needle[0]:
                if len(haystack) >= index + len(needle):
                    if haystack[index:index+len(needle)] == needle:
                        return index
        return -1
