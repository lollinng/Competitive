"""
Intuition
We have to add each element in the subarray taking count of the sum and the max answer .

let res be maximum sum and total be temporary current subarray sum
If subarray sum becames negative we discard all previous sum of the subarray and start new , since the sum would be greater if new element is not added to previous negative some array.

Approach
We use a for loop to iterate throught the array and add each element to our temporary sum(total).
We update res if temporary sum is greater than it
we reset temporary sum(total) when the subarry sum becomes 0

Complexity
Time complexity:
O(n) since we using a loop

Space complexity:
We using 2 variables hence its 0(1)

"""

class Solution:
    def maxSubArray(self, nums):
        res = -10000
        total = 0
        for i in range(len(nums)):
            total=total+nums[i]
            if res<total:
                res = total
            if total < 0:
                total=0
        return res
