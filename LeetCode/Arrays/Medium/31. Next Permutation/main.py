"""
We have to find next permuatation in lexical format i,e => [1,2,3] => [1,3,2]

Intution - 
1) after seeing example we can duduct same logic as other lexical problem in greedy 1053. Previous Permutation With One Swap, Here 
we have to find next permutation instead of past. 
2) According to pattern and logic we try to maintain descending order in the last and select pivot element s.t it disrupts descending
order .
3) we find a number greater than pivot from the right side of araay and swap it
4) Later we convert the right subarry of new pivot into ascending order for the ouput

For Eg - 0125330 => [0, 1, 2, 5, 3, 3, 0]
we can find pivot = '2' since it disrupts decending order
now max element greater than pivot is '3' from right
new array => [0, 1, 3, 5, 3, 2, 0] after swap
ans array => [0, 1, 3, 0, 2, 3, 5] after sorting subarray
hence 0125330 => 0130235 which is next biggest permutation
"""


class Solution:
    def nextPermutation(self, nums):

        n = len(nums)
        pivot = self.indexOfLastPeak(nums, n)
        if(pivot != -1):
            max_sub = self.maxSubFinder(nums, n, pivot)
            nums[pivot], nums[max_sub] = nums[max_sub], nums[pivot]
        nums[pivot+1:] = self.RearrangSub(nums[pivot+1:])
        return nums

    def indexOfLastPeak(self, nums, n):
        for i in range(n-1, 0, -1):
            if(nums[i] > nums[i-1]):
                return i-1
        return -1

    def maxSubFinder(self, nums, n, pivot):
        for i in range(n-1, pivot-1, -1):
            if(nums[i] > nums[pivot]):
                return i
        return 0

    def RearrangSub(self, sub):
        sub.sort()
        return sub


obj = Solution()
print(obj.nextPermutation([0, 1, 2, 5, 3, 3, 0]))
