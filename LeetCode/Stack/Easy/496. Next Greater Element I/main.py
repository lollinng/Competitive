from collections import deque


class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        stack = deque()
        value_dict = {}

        #  arr putting it in stack and poping/saving existing if they bigger then prev
        for i in nums2:
            while(stack and stack[-1]<i):
                value_dict[stack.pop()] = i 
            stack.append(i)

        # removing remaining elements in stack which dont have pair
        while(stack):
            value_dict[stack.pop()] = -1
        
        # returnig the dictornary values
        res = []
        for i in nums1:
            res.append(value_dict[i])    
        return res


        
