from typing import List


class Solution:
    def maximumImportance(self, n, roads):
        '''

        # we have to find the cardinitlity of every node
        iteratr through roads and updte pointer/count of every road 

        # sort cardianlity acending and assign them with thier integer values 0 to n
        in new dict

        # iterate through road again 
        and add the new values of the two nodes 

        time complexit:
        O(n)  - cardianitlitu
        O(nlogn) - sort and assing then integers
        O(n) - calculating res

        space complexity
        O(n)  - dict
        '''
        
        for v1,v2 in roads:
            cnt[v1]  = cnt.setdefault(v1,0) + 1
            cnt[v2]  = cnt.setdefault(v2,0) + 1

        sorted_list = sorted(cnt.items(),key= lambda item:item[1])

        for i in range(len(sorted_list)-1,-1,-1):
            cnt[sorted_list[i][0]] = n
            n-=1

        # print(cnt)
        res =  0
        for v1,v2 in roads:
            res+=cnt[v1] + cnt[v2]

        return res


