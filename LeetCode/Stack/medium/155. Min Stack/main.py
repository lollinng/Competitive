from collections import deque


class MinStack:
    from collections import deque
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        min_no = self.getMin()
        if val < min_no:
            min_no = val
        self.stack.append((val,min_no))
        
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float(+inf)

        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()