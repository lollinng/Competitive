import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        
        heap = []
        res = []

        for i,ele in enumerate(nums1):
            # stroing sum,index of p2
            heapq.heappush(heap,[ele+nums2[0],i,0])
            
        # pop heap for k iteration
        while k!=0 and heap:

            # Removing smallest element
            total_sum,p1_index,p2_index = heapq.heappop(heap)
            p1 = nums1[p1_index]
            res.append([p1,nums2[p2_index]])

            # adding new element to heap
            # if index remaining in p2
            if p2_index+1 < len(nums2):
                new_p2_index = p2_index+1
                new_p2 = nums2[new_p2_index]
                heapq.heappush(heap,[p1+new_p2,p1_index,new_p2_index])


            k-=1

        return res