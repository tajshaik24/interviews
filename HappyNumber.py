'''
LeetCode 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            newNum = 0
            for number in str(n):
                newNum += int(number)**2
            if newNum == 1:
                return True
            elif newNum in seen:
                return False
            seen.add(newNum)
            n = newNum
