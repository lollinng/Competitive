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
        arr1 ,arr2 = version1.split(".") , version2.split(".")
        n1 = len(arr1)
        n2 = len(arr2)
  
        for i in range(max(n1,n2)):

            if i<n1:
                num1 = int(arr1[i])
            else:
                num1 = 0

            if i<n2:
                num2 = int(arr2[i])
            else:
                num2 = 0

            if num1>num2:
                return 1
            elif num1<num2:
                return -1
            i+=1
        return 0
        