'''
LeetCode 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).
'''
class Solution:
    def fib(self, N: int) -> int:
        prev, prev_prev = 1, 0
        if(N > 1):
            for _ in range(N - 1):
                temp = prev
                prev += prev_prev
                prev_prev = temp
        return prev if N >= 1 else prev_prev
