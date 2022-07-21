class Solution:
    def peakElement(self, arr, n):

        if (n == 1):
            return 0

        for i in range(n):
            if i == 0:
                if arr[i] > arr[i+1]:
                    return i
            elif i == n-1:
                if arr[i] > arr[i-1]:
                    return i
            elif arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i

        return -1


obj = Solution()
print(obj.peakElement([1, 3, 2, 1], 3))
