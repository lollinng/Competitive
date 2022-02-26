class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = r = 0
        output = []

        while l < len(nums1) and r < len(nums2):
            if(nums1[l] < nums2[r]):
                output.append(nums1[l])
                l += 1
            else:
                output.append(nums2[r])
                r += 1
        output = nums1[l:] + nums2[r:]

        # calculate medium
        l = len(output)
        if l % 2 == 0:
            return (output[int(l/2)-1] + output[int((l)/2)]) / 2.0
        else:
            return output[int((l-1)/2)]


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
