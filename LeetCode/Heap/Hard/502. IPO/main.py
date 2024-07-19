import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        n = len(profits)
        projects = [(capital[i],profits[i]) for i in range(n)]
        projects.sort()
        max_heap = []

        i = 0
        # runnning the projects k time
        for _ in range(k):
            while i<n and projects[i][0] <= w:
                heapq.heappush(max_heap,-projects[i][1])
                i+=1

            # if no projects in budget
            if not max_heap:
                break

            # ADD MAXIMUM VALUE PROJECTS
            w-= heapq.heappop(max_heap)

        return w

                