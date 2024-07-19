class Solution:
    def search(self, nums,target):
        '''
        Since the array is descending we can try use
        a modified binary search to find the element

        here we have to fist find the index where its rotated
        then we use binary searches on remaining elements

        if we find target we return

        if left is less then mid then its normal array to left
            if target in  low<target<mid   # left side
                high = mid-1
            else:                          # right side
                low = low+1

        if left not less then mid then its descending array to left
        right side normal
            if target in mid<target<high:   # left side 
                low = low+1
            else:
                high = mid-1


        '''

        low , high = 0, len(nums)-1

        while(low<=high):
            mid = low + (high-low)//2
            if nums[mid]==target:
                return True
            
            # if low,mid,high same coz of duplicated elements skip 
            # skipp the subproblem by reducing range
            if nums[mid]==nums[low]==nums[high]:
                low+=1
                high-=1
                continue

            # if left side is normal/ in ascedning order 
            if nums[low]<=nums[mid]:
                
                if nums[low]<=target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

            # if right side normal/ in ascending order
            else:
                if nums[mid]<target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
                
        return False
