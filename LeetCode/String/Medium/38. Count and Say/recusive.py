class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
       

        x = self.countAndSay(n-1)

        # 11 -> 21 -> 1211 
        cnt = 1
        res = ''
        prev = x[0]

        for i in range(1,len(x)):
            if prev == x[i]:
                cnt+=1
            else:
                res += str(cnt)
                res += prev
                prev = str(x[i])
                cnt=1
        
        # FOR LAST ELEMENT
        res += str(cnt)
        res += prev
             
        # res = len(res) + res  
        return res