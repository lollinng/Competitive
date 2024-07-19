class Solution:
    def largestRectangleArea(self, heights):
        '''
        here we need to find the largets array of rectangle

        observations
        1) we can iterate from left to right using a pointer index
        2) we can form rectangle from prev lowest value to current index
            i.e   at 4 index the value is 2
                  prev lowest valuie is at index 1 the value is 1
                  hence reactangle area will be (curr_index - prev_index + 1 )*prev_lowest_val

        3) now to keep track of prev_indexes we will need stack which we can pop till we find element
            lesser then the current element
        4) if element size is increasing we dont calculate area , we will keep area calculation for
            while popping elements from the stack
            here while popping we will popping we will add area    (curr_index-popped_ineex)*curr_val 

        '''

        max_area = 0
        stack = deque()

        for curr_index,curr_val in enumerate(heights):
            curr_start = curr_index
            while stack and curr_val<stack[-1][1]:
                
                # popping elements and updating thier rectangular area
                prev_index,prev_value = stack.pop()
                width = curr_index-prev_index
                max_area = max(max_area,width*prev_value)

                # since current element is smaller thean all popped element we can start its block
                # form all last elements hence below case
                curr_start = prev_index    

            stack.append((curr_start,curr_val))

        # pop element/values which are in stack since they end at last index
        curr_index = len(heights)
        while(stack):
            prev_index,prev_value = stack.pop()
            width = curr_index-prev_index
            max_area = max(max_area,width*prev_value)
        
        return max_area

