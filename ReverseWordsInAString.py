'''
LeetCode 151. Reverse Words in a String

Given an input string, reverse the string word by word.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""
        s = s.strip()
        words = s.split(' ')
        while '' in words:
            words.remove('')
        for word in words:
            word = word.strip()
        left, right = 0, len(words) - 1
        while(left < right):
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -= 1
        return " ".join(words)
