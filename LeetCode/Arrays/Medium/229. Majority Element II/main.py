class Solution:
    def majorityElement(self, nums):
        
        candidate1 = candidate2 = -1
        candidate1_cnt = candidate2_cnt = 0

        for num in nums:

            if candidate1_cnt==0 and candidate2!=num:
                candidate1_cnt = 1
                candidate1 = num

            elif candidate2_cnt==0 and candidate1!=num:
                candidate2_cnt = 1
                candidate2 = num

            elif candidate1 == num:
                candidate1_cnt += 1
            elif candidate2 == num:
                candidate2_cnt += 1

            else:
                candidate1_cnt -= 1
                candidate2_cnt -= 1
          
        res = set()
        target_cnt = len(nums)/3
        
        candidate1_cnt = candidate2_cnt = 0    
        for num in nums:
            if num==candidate1:
                candidate1_cnt+=1
                
            elif num==candidate2:
                candidate2_cnt+=1
                
        if candidate1_cnt>target_cnt:
            res.add(candidate1)
        if candidate2_cnt>target_cnt:
            res.add(candidate2)
        return res

