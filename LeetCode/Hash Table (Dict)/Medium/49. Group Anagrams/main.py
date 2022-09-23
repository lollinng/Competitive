"""
Here we are trying to group all anagrams with one another

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

solution-

1) sort the word string which become list of sorted characters and join them using .join()
2) check if sorted string in dictionary if
    i) if yes then append the dictionaries previous value with current word
    ii) if no then create a key with sorted string using current word
3) return all the values of the dictionary
"""

class Solution:
    def groupAnagrams(self, strs):
        out = {}  
        for word in strs:

            # sorted(word) convert string to list with sorted characters which is converted to string back again
            temp = " ".join(sorted(word))

            if temp in out:
                out[temp].append(word)
            else:
                out[temp] = [word]
 
        return out.values()            
            

strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs)) 
            