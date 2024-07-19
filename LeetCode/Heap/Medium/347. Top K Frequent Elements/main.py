class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        new_heap = []

        # using heapify of O(n) + loop O(n) => O(2n) 
        # instaed of (heappush O(logn) and O(n) = O(logn*n))
        for i in counter:
            new_heap.append((-counter[i],i))
        heapq.heapify(new_heap)

        ans = []
        for _ in range(k):
            _ , key = heapq.heappop(new_heap)
            ans.append(key)

        return ans