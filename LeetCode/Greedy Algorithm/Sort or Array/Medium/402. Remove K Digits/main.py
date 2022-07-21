"""
Here we have to remove k digits from string such that we get lowest number.
We will be using greeddy algorithm because we can see a pettern here
Institution-
1) We try to keep the numbers in ascending order and remove those digits which are not
2) if we reach last digit but k still not 0 we remove number from right side
3) We use stack to keep track of the order of the number

Solution
1) We append digits to stack if first digit isnt 0
2) stack append if the incoming digits following ascending order
3) or else we kick the digit in last poistion in the stack untill ascending order can be seen or k==0
4) if k not 0 yet which means all number in ascending order so we remove k elements from behind
5) we return '0' if n==k or else we join all the elements present in list(stack) for ans as string


Eg - "1432219", 3
stack = [1,4] => [1,3] => [1,2] => [1,2,2] => [1,2] K FINISHED At this postion
hence we only inserting now
stack = [1,2,1,9] = 1219 
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"

        stack = []

        for d in num:
            # doesnt work for len(stack)=0 i.e first iteration
            # stack -1 tells latest number added if its greater we pop the number
            while stack and d < stack[-1] and k != 0:
                stack.pop()
                k -= 1

            # to avoid updating to stack if first element is 0 which will make ascending hard
            if stack or d != '0':
                stack.append(d)

        # print(stack,k)

        # to remove the remaining k elements from back of ascending ordered list
        if k:
            stack = stack[:-k]

        # when stack is zero there is nothing to show cases like 1234 k=4 and 10 k=1(here 0 wont get added to stack as no stack and its 0)
        if len(stack) == 0:
            return '0'
        else:
            return ''.join(stack)


obj = Solution()
print(obj.removeKdigits("1432219", 3))
