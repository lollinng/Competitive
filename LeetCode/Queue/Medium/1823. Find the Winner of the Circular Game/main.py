from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        use a queue to append element to right which are not popped
        
        run queue and add elemets to its back for k-1 iteration
        and pop the left of element qeueue without adding in kth iteration
        '''

        queue = deque([number+1 for number in range(n)])
        
        while len(queue)>1:
            for _ in range(k-1):
                ele = queue.popleft()
                queue.append(ele)
            queue.popleft()

        return queue[0]        

