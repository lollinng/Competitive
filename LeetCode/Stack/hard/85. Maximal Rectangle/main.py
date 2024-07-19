from collections import deque


class Solution:
    
    def CalculateMaxArea(self,current_height):

        max_area = 0
        stack  = deque()
        
        for curr_index,curr_val in enumerate(current_height):
            curr_start_index = curr_index
            while( stack and curr_val<stack[-1][1]):
                prev_index,prev_value = stack.pop()
                width = curr_index - prev_index
                max_area = max(max_area,width*prev_value)

                # since we start current index from the element which is next index of element lower then current
                curr_start_index = prev_index

            stack.append((curr_start_index,curr_val)) 

        # other elements which range till last index
        curr_index = len(current_height) 
        while stack:
            prev_index,prev_value = stack.pop()
            width = curr_index - prev_index
            max_area = max(max_area,width*prev_value)
        
        return max_area



    def maximalRectangle(self, matrix):
        
        if not matrix:
            return 0

        
        rows,cols = len(matrix),len(matrix[0])
        current_height = [0] * cols
        max_area  = 0

        for row in range(rows):        
            for col in range(cols):
                if matrix[row][col] == '0' :
                    current_height[col] = 0
                else:
                    current_height[col] += 1

            max_area = max(max_area,self.CalculateMaxArea(current_height))
    

        return max_area

