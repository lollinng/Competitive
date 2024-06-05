"""
here we are trying to find the minimum  number in rotated sorted array
Since its sorted array but rotated a modified binary serach can be used

Intution -
1) after caculating mid we can check if right pointer > mid pointer it should be greater if the array aint
tampered if itsn't greater we select the right side and make left = mid+1
2) we do above step untill left==right and we return the result at which both of them converged

For Eg - [4, 5, 6, 7, 0, 1, 2]  iterations-
left right mid
1) 0 6 3         we select second half ss 7>2
2) 4 6 5         we select 1st half as 1<2
3) 4 5 4         we slect 1st haf as 0<1  mid=left
4               mid=left=right
"""


class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


obj = Solution()
print(obj.findMin([4, 5, 6, 7, 0, 1, 2]))
