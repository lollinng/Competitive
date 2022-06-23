class Solution:
    def sort012(self, arr, n):
        l = 0
        r = n-1
        mid = 0

        for i in range(n):
            if(arr[mid] == 0):
                arr[mid], arr[l] = arr[l], arr[mid]
                l += 1
                mid += 1
            elif(arr[mid] == 1):
                # print("updated")
                mid += 1
            elif(arr[mid] == 2):
                arr[mid], arr[r] = arr[r], arr[mid]
                r -= 1
            # print(i,arr,mid)
        return arr


obj = Solution()
print(obj.sort012([0, 2, 1, 2, 0], 5))
