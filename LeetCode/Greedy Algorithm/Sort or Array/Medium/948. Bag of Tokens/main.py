"""
Here we are trying to find the max score in the game , 2 rules
1) we attack we gain score and lose power
2) we defence we lose score and gain power

institution:
1) the array of demons should be sorted to perform two task using pointer
2) if we can defeat a demon we gain score if we cant defeat we go in else block
3) here if score is non zero and , our power + power taken from last demon is greater than the demon we fighting we take
the power and increase our power so we can defeat more demons to max score.4
4) Example photo attached
"""


class Solution:
    def bagOfTokensScore(self, tokens, power):
        n = len(tokens)
        tokens.sort()
        score = 0
        start = 0
        end = n-1
        while(start <= end):
            if(tokens[start] <= power):
                power -= tokens[start]
                score += 1
                start += 1
            else:
                if(power+tokens[end] >= tokens[start] and score != 0 and start != end):
                    power += tokens[end]
                    score -= 1
                    end -= 1
                else:
                    break
        return score


tokens = [100, 200, 300, 400]
power = 200
obj = Solution()
print(obj.bagOfTokensScore(tokens, power))
