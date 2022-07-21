"""
Here we trying to find how many kids we can satisfy with our cookie array . Each student can have max on cookie and 
children have thier hunger index as well as the cookies

intitution-
1) sort both the array in ascending and check if cookie can fill kids hunger iteratively
2) if it does feeds the hunger go to next child
3) do this unitll last child or cookie reached

Eg -  childs = [1, 2, 3],cookies = [2, 3]
1 and 2 childs get all cookies 
"""


class Solution:
    def findContentChildren(self, g, s):
        childrens = len(g)
        cookies = len(s)
        if cookies == 0:
            return 0
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        # print(cookies)
        while(cookie != cookies and child != childrens):
            if(g[child] <= s[cookie]):
                child += 1
            cookie += 1
            # print(child,cookie)
        return child


childs = [1, 2, 3]
cookies = [2, 3]
obj = Solution()
print(obj.findContentChildren(childs, cookies))
