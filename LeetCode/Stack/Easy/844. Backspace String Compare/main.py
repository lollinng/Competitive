from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildingStack(s: str):
            stack = deque()
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return buildingStack(s) == buildingStack(t)
            
                