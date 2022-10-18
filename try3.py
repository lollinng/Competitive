
k = 2
numbers = [1,2,3,4,5,6]
low = set()
high = set()
res = []

for i in numbers:
    high.add(i+k)
    low.add(i)

for i in high:
    if i in low:
        res.append(((i-k),i))

print(res)