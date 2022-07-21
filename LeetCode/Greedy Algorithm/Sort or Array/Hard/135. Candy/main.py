"""
Here we are trying to distribute tofees to students st more grade points students get more toffes then
thier neighbors . 
We will be using greedy search becoz there is no optimal soltion requires
1) We create an array and give every student on tofee as specified
2) We will be using first loop to give tofee to students who have more grade points then left kids
3) In second loop we will be giving students more toffer then their right counteropart only if they
lesser or equal tofees then them otherwise no need to give tofee
4) we summ all the candies in the array
"""


class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candy = [1]*n

        for i in range(n-1):
            if(ratings[i] < ratings[i+1]):
                candy[i+1] = candy[i] + 1
        print(candy)
        for i in range(n-1, 0, -1):
            if(ratings[i-1] > ratings[i]):
                if(candy[i-1] <= candy[i]):
                    candy[i-1] = candy[i] + 1
        print(candy)
        return sum(candy)


obj = Solution()
print(obj.candy([1, 34, 24, 23, 23, 23, 2]))
