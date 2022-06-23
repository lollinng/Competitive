class Solution:
    def subArraySum(self, arr, n, s):

        # for little bit faster
        if(s == 0):
            for i in range(n):
                if(arr[i] == 0):
                    return [i, i]
            return [-1]

        l = 0
        sums = arr[0]
        r = 0
        while(l < n and r <= n):
            if(sums == s):
                # print(l,r,sums)
                return [l+1, r+1]
            if(sums < s and r < n-1):
                r = r + 1
                sums += arr[r]
            #   print(l,r,sums)
            # we subtract the last element and index to l
            else:
                sums -= arr[l]
                l += 1
        return [-1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
s = 15
obj = Solution()
print(obj.subArraySum(arr, n, s))
