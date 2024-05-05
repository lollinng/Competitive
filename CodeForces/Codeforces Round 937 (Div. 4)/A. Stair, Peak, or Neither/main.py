def calculate(a,b,c):
    if a<b and b<c:
        return "STAIR"
    elif a<b and b>c:
        return "PEAK"
    else:
        return "NONE"
    


k = int(input())
for _ in range(k):
    a,b,c = map(int,input().split())
    print(calculate(a,b,c))