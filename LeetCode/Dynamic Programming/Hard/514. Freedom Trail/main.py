"""
here the option is to go left or to go right

so let the mid chracter be the start of the string 
as shown in the image and the example

Greedy Method 
then we use two pointers form left and right
iterate till they find the character
this wont work coz out of all the posssible value one value could have min.
dist but the next character can be too far away form it


Hence we have to use dp to check all possible outcomes

DP
1) Recusrive method
iterate through all possible values of and check thier minimum distance
and run recursive functions through all of them to check what will the value
of the minimum ,
all recusrion will go dfs and come end in the start giving us minimum value

recusive function
1) Parameters: current index(k) in key(to find),the current character index(r) which is centre or 12:00
2) Breaking point: if current index(k) becomes greater then len(key)
3) Return min. of ( abs(current index-target index) , len(ring)-abs(current index-target index)
here both of them mention left and right way to find the target char
since one can be find in string way , other has to wrap around string hence easier to
represent it as len(ring)-abs(current index-target index)
4) Cache to store visited states



2)bottom up apporach
ring = "godding", key = "gd"
    g   o   d   d   i   n   g
--------------------------------
g |   |   |   |   |   |   |   | --  how is gd away from all chars - here we calculate g away and add d value to it
--------------------------------
d | 2 | 1  |   |   |   |   |   | -- how is d away from all chars 
--------------------------------
  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | --- dp array
--------------------------------  

Here we have dp array which is intialized with 0s
after intializing we go bottom up with filling  min_dist characters
find the minimum of every pattern of characters from the last character to front charcter
after getting last chracter 
for the next second last character we have to find squence of {second_lastchar}{last_char}
so in this case for gd whcih will be last d to g pli

"""


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        cache = {}
        
        def helper(r,k):         
            """
            r : current character index
            k : key index
            """
            if k==len(key):
                return 0
            if (r,k) in cache:
                return cache[(r,k)]
            res = float("inf")
            for i,c in enumerate(ring):
                if c==key[k]:
                    min_dest = min(
                        abs(i-r),
                        len(ring)-abs(i-r)
                    )
                    # choose the minimum of all the chracters c options
                    res = min(
                        res ,
                        min_dest +  1 + helper(i,k+1)
                    )
            cache[r,k] = res
            return res
        return helper(0,0)


        '''
        # bottom up apprach slower 
        dp = [0]*len(ring)

        for k in range(len(key)-1,-1,-1):
            next_dp=[float("inf")]*len(ring)

            # iterate through the whole ring characters and getting thier minimum dist_value
            for r in range(len(ring)):
                for i,c in enumerate(ring):
                    if c==key[k]:
                        min_dest = min(
                            abs(i-r),
                            len(ring)-abs(i-r)
                        )
                        # choose the minimum of all the chracters c options
                        next_dp[r] = min(
                            next_dp[r]  ,
                            min_dest +  1 + dp[i]
                        )
            dp = next_dp
        return dp[0]
        '''

