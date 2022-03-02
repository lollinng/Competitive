class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        l = r = 0
        res = []
        print(nums1)
        while True:
            try:
                if(nums1[l] < nums2[r]):
                    l += 1
                elif(nums1[l] > nums2[r]):
                    r += 1
                else:
                    res.append(nums1[l])
                    l += 1
                    r += 1
            except IndexError:
                break
        return res
