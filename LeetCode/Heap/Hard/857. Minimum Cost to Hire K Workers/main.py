import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        """
        
        Example 1
        w = [70,50,30]
        q = [10,20,5]
        k = 2

        each worker's pay must be directly proportional to their quality hence 
        rate = w/q
        
        pairs<rate,quality> = 
        [(7.0, 10), (2.5, 20), (6.0, 5)]
        [(2.5, 20), (6.0, 5), (7.0, 10)]

        here we try to make rate proportional by increasing everyones rate till it reaches max rate in the pair
        in better words we presume everyones rate as max of all the rates
        hence we sort array to get max rate 


        firt case : pair with quality 20,5
        1,2 pairs -> 2.5 rate needs to big as 6 rate since euqal propoetional is asked -> hence total wage = q*rate = (20+5)*6 -> 150

        Now we remove the maximum quality since we using greedy method and check other pairs
        popping 20(quality pair) with queue and adding 10(quality pair) in queue
        
        We use maxheap to remove the pair with highest quality to get greedy solution 

        second caase: pair with quality 5,7
        we have to make rate equal which is 2.5 and 7 here , toal_quality = 10+4
        2,3 pairs -> 2.4 needs to big as 7 -> hence total rate will be 7*(total quality) -> 7*14 -> 105

        hence lowest wage was 105

        Example 2 : 
        quality = [3,1,10,10,1]
        wage =[4,8,2,2,7]
        k =3
        pairs<rate,quality> = 
        [(1.3333333333333333, 3), (8.0, 1), (0.2, 10), (0.2, 10), (7.0, 1)] 
        [(0.2, 10), (0.2, 10), (1.3333333333333333, 3), (7.0, 1), (8.0, 1)]

        first case : pair with qualit 10,10,3
        1,2,3 pairs -> rate should be 1.3 -> hence total_wage = rate*total_q = 1.33*23 = 30.66
        remove 0.2,10 pair sice they have highest quality
        1,3,4 -> rate should be 7 -> wage = 7*14 = 98
        remove 0.2,10 pair sice they have highest quality
        1,3,5 -> rate should be 8 -> wage = 8*4 = 48

        hence lowest wage was 30.66

        """
        
        
        res = float('+inf')

        # pairs containig wage/quality ratio and quality itself
        pairs = []
        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i],quality[i]))
        
        print(pairs)
        pairs.sort(key=lambda x:x[0])
        print(pairs)

        max_heap = []
        toal_quality = 0
        for rate,quality in pairs:
            
            
            heapq.heappush(max_heap,-quality)
            toal_quality += quality

            if len(max_heap) > k:
                # equivalend to subtracting from total_quality since popped element is negative
                toal_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                res = min(
                    res,
                    toal_quality*rate
                )
            print(res)
        return res