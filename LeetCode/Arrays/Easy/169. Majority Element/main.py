class Solution:
    def majorityElement(self, nums):
        ele_cnt = 0
        res = -1
        for num in nums:
            if ele_cnt==0:
                ele_cnt = 1
                res = num
            elif num==res:
                ele_cnt+=1
            else:
                ele_cnt-=1


        return  res