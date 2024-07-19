class Solution:
    
    def merge(self,left,right):
        res = []
        i,j = 0,0

        while i<len(left) and j<len(right):
            # if right array element bigger
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1 
        # adding remaining elements to the result 
        res+=left[i:]
        res+=right[j:]
        return res

    def mergesort(self,nums):
        if len(nums)<=1:
            return nums
        # dividing array into 2 parts
        mid = int(len(nums)/2)
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merge(left,right)


    

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
        