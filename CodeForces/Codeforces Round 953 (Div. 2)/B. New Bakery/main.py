def solution(test_cases):
    result = []
    for n,a,b in test_cases:
        if a>=b:
            result.append(n*a)
            continue
        res = 0
        k = b-a
        if n>k:
            res += b*(b+1)//2 - a*(a+1)//2 
            res+=(n-k)*a
        else:
            res += b*(b+1)//2 - (b-n)*(b-n+1)//2 
        result.append(res)

    return result

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n,a,b = list(map(int, input().split()))
    test_cases.append((n,a,b))

results = solution(test_cases)
# results = solution([[1000000000,1000000000,1],[1000,1,1000],[5,5,11]])


for result in results:
    print(result)