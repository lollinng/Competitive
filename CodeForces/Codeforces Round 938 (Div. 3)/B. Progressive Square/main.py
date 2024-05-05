"""
Progressive Square

Given starting point , left plus and down plus
check if array has progressive square

loop over j checking validations with temp value initialized with starting point
then go down i and restart the temp value for validation

n  = 3 # arr length
a = 1 start
c = 2   i add
d = 3  j add


1   4  7
3   6  9
5   8  11

time limit exceeded

"""



def calculate(n,c,d,list_):
    a = min(list_)
    for i in range(n):
        if i==0:
            temp = a
        else:
            temp = a+(i*c)

        if temp in list_:
            list_.remove(temp)
        else: 
            return "NO"
        
        for _ in range(1,n):
            temp+=d
            if temp in list_:
                list_.remove(temp)
            else: 
                return "NO"
            
    return "YES"


"""
DONE 

Greedy Method
"""

def calculate1(n,c,d,list_):
    a = min(list_)
    new_arr_x = []
    for i in range(n):
        new_arr_x.append(a+i*c)

    new_arr_y = []
    for j in new_arr_x:
        for k in range(1,n):
            new_arr_y.append(j+k*d)
    arr =new_arr_x+new_arr_y
    arr.sort()
    list_.sort()

    if arr == list_:
        return "YES"
    else:
        return "NO"

k = int(input())
for _ in range(k):
    n,c,d = map(int,input().split())
    list_ = list(map(int,input().split()))
    print(calculate1(n,c,d,list_))