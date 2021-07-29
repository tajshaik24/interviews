'''
LeetCode 20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ')' or char == '}' or char == ']':
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if char == ')' and popped != '(':
                    return False
                if char == ']' and popped != '[':
                    return False
                if char == '}' and popped != '{':
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
