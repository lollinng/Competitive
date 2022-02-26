"""
In this flood filled algo we color the cells adjacent to our cell . 
We can either keep a visited set , of tupples(i,j) for returning if we goto same block which is frequently used in most bfs algo 
but here since we have constrain that color==new_color(avoid going to predifend cells of new color in the question iteself) 
to avoid iterting through already colored elements  

"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):

        h, w = len(image), len(image[0])
        # visited = set()       # not using this here

        def dfs(image, r, c, color, new_color):
            # makign some constraint to avoid it going overflow or iterating already iterated through or block we dont wann iterate
            if(r < 0 or c < 0 or r >= h or c >= w or color == new_color or image[r][c] != color):
                return

            # filling the color in the matrix
            image[r][c] = new_color

            # flooding into adjacent cells
            dfs(image, r+1, c, color, new_color)
            dfs(image, r-1, c, color, new_color)
            dfs(image, r, c+1, color, new_color)
            dfs(image, r, c-1, color, new_color)

        dfs(image, sr, sc, image[sr][sc], newColor)
        return image


# testing
s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
