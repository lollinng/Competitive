# Round1 Q1:

'''
Given an array of size n and an integer k where k << n. Also for each element, the absolute difference b/w its current position and sorted position is <= k. We have to sort the array.
'''

import heapq

def sort_k_sorted_array(arr, k):
    n = len(arr)
    # Initialize a min-heap
    min_heap = []
    
    # Build the initial min-heap with the first k+1 elements
    for i in range(min(k+1, n)):
        heapq.heappush(min_heap, arr[i])
    
    # Index to store the sorted elements
    sorted_index = 0
    
    # Process the remaining elements
    for i in range(k+1, n):
        arr[sorted_index] = heapq.heappop(min_heap)
        sorted_index += 1
        heapq.heappush(min_heap, arr[i])
    
    # Extract the remaining elements from the heap
    while min_heap:
        arr[sorted_index] = heapq.heappop(min_heap)
        sorted_index += 1
    