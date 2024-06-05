"""

n : final destination
k : number of points timur knows time
q : number of queries
a : distance of every point length k  
b : time of evert point length k
all remaining queries
output time taken to reach each queries he  

input struct
n k q(len(q)=3)
a1 a2 a3 if k ==
b1 b3 b3 if k=3
q1
q2
q3 



15

5 , 10 , 12 , 17

while()

"""


def run(n,k,q,a,b,q_list):
    speed = []
    for i in range(k):
        speed.append(a[i]/b[i])
    
    res = ''
    for q_stop in q_list:
        mini_time = 0
        j = 0
        print(a,speed,q_stop)
        for j in range(k):
             
            if q_stop>=a[j]:
                mini_time += (a[j]-a[j-1])/speed[j]
            else:
                if j==0:
                    mini_time += (q_stop)/speed[j]
                else:
                    mini_time += (q_stop-a[j-1])/speed[j]
        
        res+= " " + str(int(mini_time))
    return res

loop = int(input())
for _ in range(loop):
    n,k,q = [int(x) for x in input().split(" ")]
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    q_list = []
    for _ in range(q):
        q_list.append(int(input()))
    print(run(n,k,q,a,b,q_list))