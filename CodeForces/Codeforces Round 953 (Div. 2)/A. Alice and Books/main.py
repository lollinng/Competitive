def solution(test_cases):
    result = []
    for _,pages in test_cases:
        result.append(max(pages[:-1])+pages[-1])
    return result

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    pages = list(map(int, input().split()))
    test_cases.append((n, pages))

results = solution(test_cases)

for result in results:
    print(result)