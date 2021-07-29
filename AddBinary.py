'''
LeetCode 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        lenStrA, lenStrB = len(a) - 1, len(b) - 1
        minLength = min(lenStrA, lenStrB)
        carryOne = False
        while(minLength >= 0):
            sumTotal = int(a[lenStrA]) + int(b[lenStrB])
            if carryOne:
                sumTotal += 1
                carryOne = False
            if sumTotal >= 2:
                carryOne = True
                sumTotal -= 2
            result = str(sumTotal) + result
            lenStrA -= 1
            minLength -= 1
            lenStrB -= 1
        while lenStrA >= 0:
            charA = int(a[lenStrA])
            if carryOne:
                charA += 1
                carryOne = False
            if charA >= 2:
                carryOne = True
                charA -= 2
            result = str(charA) + result
            lenStrA -= 1
        while lenStrB >= 0:
            charB = int(b[lenStrB])
            if carryOne:
                charB += 1
                carryOne = False
            if charB >= 2:
                carryOne = True
                charB -= 2
            result = str(charB) + result
            lenStrB -= 1
        if carryOne:
            result = "1" + result
        return result
