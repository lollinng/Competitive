"""
                  fun([ 3, 1, 2 , 9, 3 ])
                    /                        \
            3 + fun([2,9,3])            fun([1,2,9,3]) _______
                /        \                       /            \
         2 + fun([3])  fun([9,3])       1+ fun([9,3])   fun([2,9,3])      
               |          |                   |               /     \
               3       max(9,3)           max(9,3)   2+fun([3])    fun([9,3])
                                                           |           |
                                                           3        max(9,3)
"""


class Solution():
    def rob(self, arr) -> int:
        self.data = arr
        self.totalElements = len(arr)
        self.dp = [-1]*(self.totalElements+1)
        return self.recursive(0)

    # Here we are passing index from where we need to start selection..

    def recursive(self, i):
        if self.dp[i] != -1:
            print(i, self.dp[i], "Already have answer :) ")
            return self.dp[i]

        t = self.totalElements - i
        if t == 0:
            self.dp[i] = 0
        elif t == 1:
            self.dp[i] = self.data[-1]
        elif t == 2:
            self.dp[i] = max(self.data[-1], self.data[-2])
        else:
            self.dp[i] = max(self.data[i] + self.recursive(i+2),
                             self.recursive(i+1))
        # Few consoles for better visualization..
        print(i, self.dp[i], "calculation :( ")
        return self.dp[i]


s = Solution()
print(s.rob([2, 1, 1, 2]))
# ans - 4
