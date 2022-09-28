class Solution():

    def __init__(self,n,numbers):
        self.n = n
        self.numbers = numbers

    def run(self):
        res = 0
        for left in range(self.n):
            max_val = self.numbers[left]
            min_val = self.numbers[left]
            for right in range(left,self.n):
                lists = self.numbers[left:right+1]

                # if(max)

                max_val = max(lists)
                min_val = min(lists)
                if max_val%min_val==0:
                    res+=1
        return res

inputs = int(input())
for i in range(inputs):
    n = int(input())

    nummbers = input().split()
    for i in range(n):
        nummbers[i] = int(nummbers[i])

    obj = Solution(n,nummbers)
    print(obj.run())