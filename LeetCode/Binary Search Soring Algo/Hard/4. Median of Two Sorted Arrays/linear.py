class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        l = r = 0
        
        nums1_len,nums2_len = len(nums1),len(nums2)
        tot_len = nums1_len +nums2_len
        odd = tot_len % 2 == 1
        index1,index2 =  (tot_len-1)//2 , tot_len//2
        
        res = []
        for index in range(index2+1):
            if l<nums1_len and r< nums2_len:
                if nums1[l] <= nums2[r]:
                    curr_ele = nums1[l]
                    l+=1
                else:
                    curr_ele = nums2[r]
                    r+=1
            elif l<nums1_len:
                curr_ele = nums1[l]
                l+=1
            else:
                curr_ele = nums2[r]
                r+=1
            
            if index==index1 or index==index2:
                res.append(curr_ele)

        if odd:
            return res[0]
        else:
            return (res[0]+res[1])/2
        

        