class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast:
                break

        # now second part finding starting paart of cycle
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]

            
        return slow
        