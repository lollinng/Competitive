from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        # list1_  = [ch for ch in s]
        # list2_  = [ch for ch in t]
        # list1_.sort()
        # list2_.sort()
        # return True if list1_ == list2_ else False

    
        # list2_  = [ch for ch in t]
        # for i in s:
        #     if i in list2_:
        #         list2_.remove(i)
        #     else:
        #         return False
        # return True if len(list2_)==0 else False

        # return True if sorted(s) == sorted(t) else False
        if len(s) != len(t):
            return False          
        return Counter(s) == Counter(t)
