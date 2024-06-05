class Solution:
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)

        for i in range(n,-1,-1):
            bigger_cnt = 0
            for j in range(n):
                if nums[j]>=i:
                    bigger_cnt+=1

            if bigger_cnt == i:
                return bigger_cnt
        return -1


        