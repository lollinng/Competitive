class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, n):

        # stack appends and pops indexes of the array
        stack = [0]
        span = [-1]*n
        stack.append(0)
        for i in range(n):
            while(len(stack) != 0 and a[stack[-1]] <= a[i]):
                stack.pop()
            if(len(stack) == 0):
                span[i] = i+1
            else:
                span[i] = i - stack[-1]
            stack.append(i)
        return span


obj = Solution()
# print(obj.calculateSpan([10, 4, 5, 90, 120, 80], 6))



print(dp)
# print(dp[100][100)
print(len(dp))
