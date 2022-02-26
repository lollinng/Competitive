class Solution:
    def sortedSquares(self, A):
        ans = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        # so that we can check in absolute value
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                ans[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                ans[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return ans


x = Solution()
print(x.sortedSquares([-4, -1, 0, 3, 10]))
