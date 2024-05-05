""""

3






"""

def calculate(n):
    cnt_1 = 0
    for _ in range(2*n):
        cnt = 0
        temp = ''
        for _ in range(0,2*n,2):
            if cnt_1==0 or cnt_1==1:
                if cnt == 0 :
                    temp+= "##"
                    cnt+=1
                else:
                    temp+= ".."
                    cnt-=1
            else:
                if cnt == 0 :
                    temp+= ".."
                    cnt+=1
                else:
                    temp+= "##"
                    cnt-=1
        
        print(temp)    
        if cnt_1==3:
            cnt_1=0
        else:
            cnt_1+=1
        
    pass

k = int(input())
for _ in range(k):
    calculate(int(input()))