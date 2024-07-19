class Solution:
    
    def resolve(self,a,b,operand):
        if operand == '+':
            res = a+b
        elif operand=='-':
            res = a-b
        elif operand =='*':
            res = a*b
        else:
            res = int(a/b)
        return res


    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque()

        operands = ['+','-','*','/']

        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                res = self.resolve(a,b,i)
                stack.append(res)
        return stack.pop()
