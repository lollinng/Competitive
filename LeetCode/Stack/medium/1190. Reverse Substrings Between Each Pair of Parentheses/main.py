from collections import deque


class Solution:
    '''
    We will need a helper which will reverse the string inside the 
    '''
    def reverseParentheses(self, s: str) -> str:
 
        stack = deque()
        for char in s:
            if char!=')':
                stack.append(char)
            else:
                temp = []
                while stack[-1]!='(':
                    temp.append(stack.pop())

                stack.pop()
                stack.extend(temp)

        return "".join(stack)
            

