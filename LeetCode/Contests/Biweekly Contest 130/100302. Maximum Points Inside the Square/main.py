"""
Intuition

1) Get max of tuple
2) stop the square upon reaching max of the char occuring second time


return : max points that can come
"""




class Solution:
    def maxPointsInsideSquare(self, points, s):
        
        
        dict_ = {}
        n = len(points)
        i = 0 
        max_length = float('+inf')
        flag = False
        # calculating max_len
        while(i<n):

            max_ = max(abs(points[i][0]),abs(points[i][1]))
            if  s[i] in dict_:
                # if new collision more less
                if  dict_[s[i]] > max_:

                    if max_length> dict_[s[i]]-1:
                        max_length = dict_[s[i]]-1
                    dict_[s[i]] = max_
                elif dict_[s[i]] == max_:
                    if max_length>=max_:
                        max_length = max_ -1
                else:
                    # if new collison is bigger then existing one

                    # if new collison is smaller then max_lem


                    if max_length>=max_:
                        max_length = max_-1
            else:
                dict_[s[i]] = max_
            print(dict_,max_,max_length)
            i+=1
           
        
        # check how many points inside max_length
        res = 0
        for i in dict_.values():
            if i <= max_length :
                res += 1
        return res


        
# points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]
# points =  [[1,1],[-2,-2],[-2,2]]
# points = [[1,1],[-1,-1],[2,-2]]
# points =  [[1,1]]
# points =  [[-6,-4],[8,-1],[3,9]]
# points =  [[-1,-4],[16,-8],[13,-3],[-12,0]]
# s = "abdca"
# s = "abb"
# s = "ccd"
# s = "a"
# s = "ccc"
# s = "abda"

points = [[16,32],[27,3],[23,-14],[-32,-16],[-3,26],[-14,33]]
s = "aaabfc"

# points = [[10,-12],[-5,-4],[-7,15],[9,16]]
# s = "dada"

obj = Solution()
print(obj.maxPointsInsideSquare(points,s))