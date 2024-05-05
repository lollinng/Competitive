"""
value :  count
a : one
b : two
  :  n

minimum for m

Intution:
We face two choices choose a or b
and we have to find minimum

hence dp problem , minimum knapsack problem

recursion 
params: curr_number of yogurts ,total
choices : select a or select b
return : minimum of the choices

# Recusive solution
# k = int(input())

# def recursion(count,total,cache):
#     # getting out
#     if count==n:
#         return total
#     if cache[count] != -1:
#         return cache[count]
    
#     # select a
#     res_a = recursion(count+1,total+a,cache)
#     # select b
#     res_b=float("+inf")
#     if count+2<=n:
#         res_b = recursion(count+2,total+b,cache)
        
#     cache[count] = min(res_a,res_b)
#     return cache[count]

# for i in range(k):
#     n,a,b = [int(x) for x in input().split(" ")]
#     cache = [-1]*(n+1)
#     print(recursion(0,0,cache))


Greedy
                __
            1         2
        1      2    1      2
    1     2  1    2

    
eg n = 8 -- means 8 yogurt count to buy

1*8 = 8   , value 8*a
2 * 4 = 8 , value 4*b

here we can see that if 
2a>b then all should be a
b>2a then all should be b and if odd then one a should be added 

"""


k = int(input())
for i in range(k):
    n,a,b = map(int ,input().split(" "))
    res = 0
    if n%2 == 0:
        res = min(n*a,n//2*b)
    else:
        res = min(n*a,n//2*b+a)
    print(res)
