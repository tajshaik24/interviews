'''
LeetCode 736. Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let-expression is the value of the expression expr.
An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.

A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.

For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.

Note:
The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def evaluate(self, expression: str) -> int:
        return calc(expression)

def split_args(expression):
    stack = []
    result = []
    start = 0
    for i, c in enumerate(list(expression)):
        if c == " " and not stack:
            result.append(expression[start:i])
            start = i + 1
        if c == "(": stack.append("(")
        if c == ")": stack.pop()
    result.append(expression[start:])
    return result

def calc(expression:str, m={}):
    if expression[0] != '(':
        if expression[0].isdigit() or expression[0] == '-':
            return expression
        else:
            return m[expression]
    expression = expression[1:-1]
    cmd, expression = expression.split(" ", 1)
    args = split_args(expression)
    if cmd == 'add':
        return str(int(calc(args[0], m)) + int(calc(args[1], m)))
    if cmd == 'mult':
        return str(int(calc(args[0], m)) * int(calc(args[1], m)))
    if cmd == 'let':
        n = dict(m)
        for i in range((len(args) - 1) // 2):
            n[args[2*i]] = calc(args[2*i + 1], n)
        return calc(args[-1], n)
