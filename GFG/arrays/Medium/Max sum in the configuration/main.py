"""
here we want to use n complexity but we have to rotate as well as find the max value of array in the rotation which
will cost n^2 complexity

so we created a equation to solve it in On
lets take array = [a,b,c,d]
thier index sum 
S0 = a*0 + b*1 + c*2 + d*3
S1 = a*1 + b*2 + c*3 + d*0
S3 = a*2 + b*3 + c*0 + d*1
we have to find max of S 0,1,2 and 3

so  by looking on the pattern
we can try
S1 =  S0 + (a+b+c+d) - 4d                 # 4d to elemenate d completely
S1 =  S0 + TotalSum - n*(last_element)
Sn+1 =  Sn + TotalSum - n*array[n-1-i]           # where i will be index
"""


def max_sum(a, n):
    initialSum = 0
    TotalSum = 0
    for i in range(n):
        initialSum += i*a[i]
        TotalSum += a[i]

    ans = initialSum
    # the below equation is derived from a calculation show above
    # a[n-1-i] is the last element of the array
    for i in range(0, n):
        # print(initialSum + TotalSum - n*a[n-1-i])
        initialSum = initialSum + TotalSum - n*a[n-1-i]
        ans = max(ans, initialSum)
    return ans


print(max_sum([8, 3, 1, 2], 4))
