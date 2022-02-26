class Solution:
    # using dict
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     num_dict = {}
    #     for i,num in enumerate(numbers):
    #         val = target - num
    #         if val in num_dict:
    #             return [num_dict[val]+1,i+1]
    #         num_dict[num] = i
    #         print(num_dict)
    #     return []

    # using pointers , faster comparatively
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1
        while r >= l:
            res = numbers[r] + numbers[l]
            if res == target:
                return [l+1, r+1]
            elif res > target:
                r -= 1
            else:
                l += 1


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
