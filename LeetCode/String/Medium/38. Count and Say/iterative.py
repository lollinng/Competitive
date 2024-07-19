class Solution:
    def countAndSay(self, n: int) -> str:
        
        dp = [''] * n
        dp[0] = "1"
        for i in range(1,n):
            cnt = 1
            x = dp[i-1]
            prev_ele = x[0]
            res = ""
            for j in range(1,len(x)):
                if prev_ele == x[j]:
                    cnt+=1
                else:
                    res+=str(cnt)
                    res+=prev_ele
                    prev_ele = x[j]
                    cnt = 1

            # for last_element
            res+=str(cnt)
            res+=prev_ele
            dp[i] = res

        return dp[-1]