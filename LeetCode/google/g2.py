'''

Medium Question from LC. I was asked to get all the possible combinations of a series of "musical notes" given the following rules:

Every sequence must have a sum of 12
Possible notes that make up the sequence can only be 1, 2 and 3
There are only certain valid transitions, they're given in this dictionary {1: [2, 3], 2: [1, 2], 3: [1]}. Meaning, only 2 and 3 are allowed after 1 and so on
First note and last note must have a valid transition. Example of valid sequence: [1, 2, 2, 2, 1, 1, 3]. Example of not valid: [1, 2, 2, 2, 2, 2, 1] reason is because 1 cannot be followed by another 1 (last and first notes transition is invalid)
Return every possible valid sequence in an array of possible sequences. You may return it in any order.

My approach was to make a DFS algorithm to go through every possible combination. Before calling recursively my function i'd check if it's valid transition and sum is not above 12

Interviewer later would ask me about time and space complexity which was a bit hard for me but came up with exponential order for both. In the worst case scenario
'''

class Solution:


    def generate_musical_notes(target_sum):

        res = []

        def dfs(index,path,path_sum):
                        
            if target_sum == path_sum:
                res.append(path[:])
            
            if target_sum < path_sum:
                return

            # recursion
            if path[-1]==1:
                dfs(index+1,path+[2],path_sum+2)
                dfs(index+1,path+[3],path_sum+3)
            elif path[-1]==2:
                dfs(index+1,path+[1],path_sum+1)
                dfs(index+1,path+[2],path_sum+2)
            else:
                dfs(index+1,path+[3],path_sum+1)

            
        for i in range(3):
            dfs(1,[i],i)

        return res

    