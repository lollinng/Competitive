class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left

    def feasible(self, bloomDay, waitingDays, m, k):
        bouquetCount = 0
        requiredFlowers = k
        for day in bloomDay:
            if day <= waitingDays:
                requiredFlowers -= 1
                if requiredFlowers == 0:
                    bouquetCount += 1
                    requiredFlowers = k
            else:
                requiredFlowers = k
            
        return bouquetCount>=m