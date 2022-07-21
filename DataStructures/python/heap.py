import heapq

pq = [1, 2, -34, 54, 6, 2]
# pq = [(-2, 'a'), (-1, 'b')]

# min heap
heapq.heapify(pq)
max = heapq.heappop(pq)
print(max)

# max heap
pq = [-x for x in pq]
heapq.heapify(pq)
max = heapq.heappop(pq)
print(-max)

# add element to heap
heapq.heappush(pq, -92)
max = heapq.heappop(pq)
print(-max)
