"""
Here We are trying to find the largest subarray length where each elements is present only in 1 on array .

Intuition -
1) first we find the last index of character in string of each character in the string
2) We iterate till the last index(right) of the string comes , if i==right then we get the score(len of substring)
3) if we get last value of char >  value of max/right we update the max s.t the new char. last index also gets 
in substring
4) score is used to calucate len of each sub string

Example - "ababcbacadefegdehijhklij"
we get last = {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 
'l': 21}
we iterate from i to n
1)right = 8 hence ababcbaca is taken as first string with len = 9
2)right = 15 hence defegde is taken as second string with len=7
3)right = 19 => gets updated to 22 (coz of i)=>23 hence  hijhklij is last string with len =8
hence answer is [9,7,8]
"""


class Solution:
    def partitionLabels(self, s):
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        print(last)
        right = 0
        res = []
        score = 1
        for i in range(n):
            if(last[s[i]] > right):
                right = last[s[i]]
            if(i == right):
                res.append(score)
                score = 0
            score += 1
        return res


obj = Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))
