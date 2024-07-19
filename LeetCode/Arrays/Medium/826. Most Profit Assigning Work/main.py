class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = sorted(zip(profit,difficulty),reverse=True)
        worker.sort(reverse =True)
        no_of_workers = len(worker)
        worker_ptr = 0
        res = 0
        for money,difficult in arr:
            while worker_ptr<no_of_workers and worker[worker_ptr] >=difficult:
                res+=money
                worker_ptr+=1
        return res
  