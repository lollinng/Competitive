from collections import Counter

tasks = ["A", "b", "c", "A", "b", "A"]
freq = Counter(tasks)                   # Counter({'A': 3, 'b': 2, 'c': 1})
print(freq.items())               # dict_items([('A', 3), ('b', 2), ('c', 1)])
print(freq.values())                    # dict_values([3, 2, 1])
# list_ = list(freq.values()) = [3,2,1]
# max = max(freq.values()) = 3


# to count characters in string
st = Counter("abcsds")
print(st)

# convert dictionary into list of tupples
c = Counter("abcsds")        # creating dictionary
print(c.items())
