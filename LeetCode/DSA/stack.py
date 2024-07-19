from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('b')

print(stack)
print(len(stack))
print(stack[0])
print("front element",stack[-1])
