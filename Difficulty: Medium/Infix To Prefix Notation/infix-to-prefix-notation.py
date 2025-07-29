class Solution:

    def isOperator(self, ch):
        return ch in "+-*/^"

    def operatorPrecedence(self, op):
        if op == '^':
            return 3
        elif op in '*/':
            return 2
        elif op in '+-':
            return 1
        return -1

    def convertInfixToPostfix(self, s):
        stack = []
        res = []

        for ch in s:
            if ch.isalnum():
                res.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                if stack:
                    stack.pop()  # pop '('
            else:
                while (stack and self.operatorPrecedence(ch)
                       <= self.operatorPrecedence(stack[-1])):
                    res.append(stack.pop())
                stack.append(ch)

        while stack:
            res.append(stack.pop())

        return ''.join(res)

    def infixToPrefix(self, s):
        # Reverse the string and swap '(' with ')'
        s = s[::-1]
        s = ''.join(
            ['(' if ch == ')' else ')' if ch == '(' else ch for ch in s])

        postfix = self.convertInfixToPostfix(s)
        return postfix[::-1]