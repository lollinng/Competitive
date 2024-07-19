def dfs(n,visited,target,path,total_sum,memo):

    # Use memoization to avoid redundant calculations
    state = (frozenset(visited), total_sum)
    if state in memo:
        return memo[state]

    # breaking condition
    if total_sum > target:
        return None
    
    # positive condition
    if len(path) ==n and  total_sum==target:
        return path
    
    for i in range(1,n+1):
        if i not in visited:
            visited.add(i)

            total_sum_temp =  total_sum+ abs(i-(len(path)+1))
            res = dfs(n,visited,target,path+[i],total_sum_temp,memo)
            
            if res is not None:
                return res
               
            visited.remove(i)
    memo[state] = None
    return None


def solution(test_cases):
    result = []
    for n,k in test_cases:
        
        if n*(n+1)//2 < k:
            result.append("No")
            continue
        
        res = dfs(n,set(),k,[],0,{})
        if res is None:
            result.append("No")
            continue

        result.append("Yes")
        result.append(res)
        print(result)
    return result

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n,k = list(map(int, input().split()))
    test_cases.append((n,k))

results = solution(test_cases)
# results = solution([[1000000000,1000000000,1],[1000,1,1000],[5,5,11]])


for result in results:
    print(result)