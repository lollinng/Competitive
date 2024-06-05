


def run(p1,p2,p3):


    total_sum = p1+p2+p3
    if total_sum==0 :
        return 0
    
    if  total_sum%2 != 0 :
        return -1
    

    if p1==0:
        return min(p2,p3)
    
    

    draw = 2
    p1-=1
    p2-=1
    p3-=1

    while(p1!=0):
        draw+=1
        p1-=1
        p3-=1
    
    while(p2!=0 and p3!=0):
        draw+=1
        p2-=1
        p3-=1
    
    
    return draw

loop = int(input())
for _ in range(loop):
    n,k,q = [int(x) for x in input().split(" ")]
    print(run(n,k,q))
