"""
In this problem we have to find which version number bigger or latest

Example 1:

Input: version1 = "1.01", version2 = "1.001" equal
Input: version1 = "1.0", version2 = "1.0.0"  equal
Input: version1 = "0.1", version2 = "1.1"    v2 bigger

Solution:
1) Split according to the decimal points in the array as ints
2) Iterate till the max of the two arrays as the missing will be takes as 0 as shown in 3 examples
3) If ith index less than array size of a version take its value inside array otherwise take 0
4) COmpare the sizes if someone bigger return appropirate value

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        ver1 = [int(i) for i in ver1]
        ver2 = [int(i) for i in ver2]

        # print(int('001')==int('01'))  
        n1 = len(ver1)
        n2 = len(ver2)
        max_ = max(n1,n2)
        for i in range(max_):

            # if i>=n1:
            #     if ver2[i]>0:
            #         return -1
            #     continue
            # elif i>=n2:
            #     if ver1[i]>0:
            #         return 1
            #     continue

            # if ver1[i]>ver2[i]:
            #     return 1
            # elif ver2[i]>ver1[i]:
            #     return -1



            # Instead of adding extra conditions just add value 0 to non existent 
            if i<n1:
                a = ver1[i]
            else:
                a = 0

            if i<n2:
                b = ver2[i]
            else:
                b = 0
            

            
            if  a>b:
                return 1
            elif b>a:
                return -1
        
        return 0
        