"""
here we are trying to give change for customer for paying for lemonade $5 with $5,10,20 deomination

intuition - 
1) if customer pays 5 we increment 5 pointer
2) if customer pays 10 we increment 10 pointer and decrement 5 pointer
3) if customer pays 20 , we either do following things -
i) if no 10 denomination ,we give 5's 3 denomination
ii) if 10 denomination there ,we decrement 5 and 10 
"""


class Solution:
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
                five -= 1
            else:
                # for providing 20 spare if u dont have tens
                if(ten <= 0):
                    five -= 3
                else:
                    five -= 1
                    ten -= 1
            if ten < 0 or five < 0:
                return False
            # print(dicti)
        return True


obj = Solution()
print(obj.lemonadeChange([5, 5, 10, 20, 5, 5, 5,
      5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
