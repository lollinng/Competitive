
# import math as mt
# import collections as cll
import bisect
 
 
MOD = 10**9 + 7
INF = float('inf')
NINF = float('-inf')
 
 
def lb(nums,x):
    # nums = sorted(nums)
    return bisect.bisect_left(nums,x)
def ub(nums,x):
    # nums = sorted(nums)
    return bisect.bisect_right(nums,x)
def inp():
    return int(input())
def sinp():
    return input().strip()
def linp():
    return list(map(int,input().split()))
def lsinp():
    return list(map(str,input().strip().split()))
def minp():
    return map(int,input().split())
def msinp():
    return map(str,input().strip().split())
 
 
# Always remember to check 'ub' and 'lb' if used.
 
 
 
def solve():
    n, k, q = map(int, input().split())
    a = [0] + linp()
    b = [0] + linp()
    for _ in range(q):
        in_val = inp()
        ind = lb(a,in_val)
        if ind == 0:
            print(0,end=" ")
            continue
        # if ind == k+1:
        #     ind-=1
        if a[ind] == in_val:
            print(b[ind])
            continue
        sp = (a[ind] - a[ind - 1]) / (b[ind] - b[ind - 1])
        # print(sp)
        ind-=1
        antar = in_val - a[ind]
        t = antar / sp
        print(int(b[ind] + t), end=" ")
    print()
 
 
 
for i in range(int(input())):
    solve()