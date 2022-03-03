# USING LIST
q = []

# Adding elements to the queue
q.append('a')
q.append('b')
q.append('c')
q.append((1, 2))
print("Initial q")
print(q)

# Removing elements from the queue
print("\nElements deqd from queue")
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print("\queue after removing elements")
print(q)
