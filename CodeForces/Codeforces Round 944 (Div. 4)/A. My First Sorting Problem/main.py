

z = int(input())
for _ in range(z):
    x,y = [int(x) for x in input().split(" ")]
    if x > y:
        print(y,x)
    else:
        print(x,y)