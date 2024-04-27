"""
In this problem we have to find element in a rotated array
To find element 0(n) linear search is go to but since we have 
been asked to solve it in O(log(n)) and sorted array we will use binary search

Here we the pattern of the rotated arrray looks like 
4 5 6 7 0 1 2   target = 0
1) One side of the mid element is sorted hence we can only use binary search in that direction
2) We first find sorted side by checking mid with left and right pointers
3) after finding soted side we check if element in that side using 
    In left side sorted problem like above
    nums[left]<=target and target < nums[mid]: 
    here in left side we check if leftmost element smaller than target and target lesser than mid
    if thats true then target resides in left side hence right = mid-1
    else target reside in right side hence left = mid+1

    same process for right side sorted array

4)  we return the index if mid becomes target's index    


"""



class Solution:
    def search(self, nums, target):
        left,right = 0 ,len(nums)-1

        while(left<=right):
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            # left sorted portionn 
            if nums[left]<=nums[mid]: 
                if nums[left]<=target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1

            # right sorted problem
            else:
                if nums[mid]< target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

        