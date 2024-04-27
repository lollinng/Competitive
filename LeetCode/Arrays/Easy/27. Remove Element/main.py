class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        return k
 
class Solution:
    def removeElement(self, nums, val):
        j = len(nums)
        i = 0
        ans = 0
        while(i<j):
            if nums[i] == val:
                nums[i] = nums[j-1]
                j-=1
                ans +=1
            else:
                i+=1
        return  len(nums) - ans