"""

Time limit exceeded

"""

def calculate(n,k,list_):
    res = 0
    i = 0
  
    while i!=k and len(list_)!=0:

        # kraken attacks behind
        if i%2 == 0:
            list_[0] -=1
            if list_[0] == 0:
                res+=1
                list_.pop(0)
        else: 
            list_[-1] -=1
            if list_[-1] == 0:
                res+=1
                list_.pop(-1)
        i+=1
    return res
 
 





k = int(input())
for _ in range(k):
    n,k = map(int,input().split())
    list_ = list(map(int,input().split()))
    print(calculate(n,k,list_))