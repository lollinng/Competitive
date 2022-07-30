"""
Here we are trying to make all number same by decresing one and increasing other as 1 task .

intuition-
1) here we take median as target and calulate the steps needed by the left side to reach that median
2) Since its given gaurenteed solution we dont care abt right side
3) now wer create the mentioned array and traverse throguht the element adding the steps or diff betw
the target and the value of curent element
"""


class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*n
        sums = 0
        for i in range(n):
            arr[i] = (2*i)+1
            sums += arr[i]
        target = int(sums/n)  # median for both odd and even arrays
        left, res = 0, 0
        while(arr[left] < target):
            res += target - arr[left]
            left += 1
        return res


obj = Solution()
print(obj.minOperations(6))  # [1, 3, 5, 7, 9, 11]
