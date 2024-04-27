"""
Here we are trying to group anagrams together,
common pattern between anagrams is they look same when sorted like bac and cba will become abc

Solution : 
1) have a dict to store all basic form of anagrams in them and thier value contains real string words
2) Iterte through list sort the word check if anagram in dict if yus then append the new word to that anagram key
3) If not then create a key value pair of sorted and real word in dict
4) return list of all the values 

"""

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for word in strs:
            # creating sorted word for indentifying anagrams    
            sorted_word = "".join(sorted(word))

            # inserting i into already exusted anagram
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
            # if i doesnt have anogram add into dictionary and to the list 
                anagrams[sorted_word] = [word]
        return list(anagrams.values())
   