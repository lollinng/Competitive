def run(a,b,c,d ):


    flag_l = flag_r = False 

    i = a
    while(True):
        if (i==13):
            i=1  
        if(i==b):
            break
        if i == d or i == c :
            flag_l = True
            break
        i+=1

    i = b
    while(True):
        if (i==13):
            i=1
        if(i==a):
            break
        if i == d or i == c :
            flag_r = True
            break
        i+=1

    
    if flag_l and flag_r:
        return"YES"
    return "NO"
    



loop = int(input())
for _ in range(loop):
    a,b,c,d = [int(x) for x in input().split(' ')]
    print(run(a,b,c,d))


# from generator import a as z

# loop = z[0]
# for i in range(1,len(z)):
#     a,b,c,d = [int(x) for x in z[i].split(' ')]
#     print(run(a,b,c,d))

# 3 12 11 8


# 12 1 10 2
# 3 12 6 9
# 1 9 8 4
