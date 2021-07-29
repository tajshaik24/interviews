'''
LeetCode 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(n, s, op, cp):
            nonlocal result
            if(len(s) == 2*n):
                result.append(s)
            if op < n:
                helper(n, s + "(", op + 1, cp)
            if cp < n and op > cp:
                helper(n, s + ")", op, cp + 1)
        helper(n, "", 0, 0)
        return result


