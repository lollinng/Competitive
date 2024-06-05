import heapq

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    hp = []

    if a > 0:
        heapq.heappush(hp, -a)
    if b > 0:
        heapq.heappush(hp, -b)
    if c > 0:
        heapq.heappush(hp, -c)

    res = 0

    while len(hp) > 1:
        print(a,b,hp)
        a = -heapq.heappop(hp)
        b = -heapq.heappop(hp)
        a -= 1
        b -= 1
        res += 1

        print(a,b,hp)
        if a > 0:
            heapq.heappush(hp, -a)
        if b > 0:
            heapq.heappush(hp, -b)

    if hp and hp[0] % 2:
        print(-1)
        continue

    print(res)