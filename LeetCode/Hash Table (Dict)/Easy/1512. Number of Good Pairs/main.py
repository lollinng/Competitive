class Solution:
    def numIdenticalPairs(self, nums):
        hash_map = {}
        res = 0
        for c in nums:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                res += hash_map[c]
                hash_map[c] += 1
            print(c, hash_map, res)
        return res
