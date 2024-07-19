class Solution:
    def largestDivisibleSubset(self, nums):
        len_nums = len(nums)
        if len_nums<2:
            return nums
        
        nums.sort()

        # store the dp solution
        # which stores the len of largest divisible subsert ending at index i
        dp = [1]*len_nums

        # storing the index of the previous element in the largest divisible subsetd
        # at each index
        prev_index = [-1]*len_nums
        
        max_len = 1 
        max_index = 0  # index of the last element in the largest divisible subset

        for right in range(1,len_nums):
            for left in range(right):
                # check if num[r] is divisble by nums[l]
                # and check current largest value in dp is less then the left's largest value +1 (since one element will be added to arr)
                if nums[right]%nums[left]==0 and dp[right]<dp[left]+1:
                    dp[right] = dp[left]+1
                    prev_index[right] = left   # setting prev_index for letter accessing the array
                    # updating max_len
                    if dp[right]>max_len:
                        max_len = dp[right]
                        max_index = right
        '''
        print(prev_index)
        print(max_index)
        print(dp)

        for [1,2,3]
        [-1, 0, 0]
        1
        [1, 2, 2]
        
        for [1,2,3]
        [-1, 0, 1, 2]
        3
        [1, 2, 3, 4]

        '''
        # Reconnecting max_index's biggest subarray in revserse order for answer
        subset = []
        while max_index!=-1:
            subset.append(nums[max_index])
            max_index = prev_index[max_index]

        return subset[::-1]


