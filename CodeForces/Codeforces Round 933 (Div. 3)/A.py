itr = int(input())
for i in range(itr):

    n,m,k = [ int(i) for i in input().split(" ")]
    b = [ int(i) for i in input().split(" ")]
    c = [ int(i) for i in input().split(" ")]

    res = []
    for i in (b):
        for j in (c):
            if i+j < k:
                res.append([i,j])

    print(len(res))

"""
4 4 8
1 5 10 14
2 1 8 1
o/p - 6

"""






