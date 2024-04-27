"""
Here we to find the largest substring lenght which can be made by replacing 
a single type of character k times 
for eg - AABABBA with k=1 will become AABBBBA

Intution:
1) We have to use largest substring algorithm using sliding window
2) but we have to check curr_len subsrtring if its bigger than (max of any element + k)
then we have a problem else the substring is good to count as res
3) Upon curr_len bigger its invalid string which we nullify by updating l in sliding winodw
and decrementing the l in dictionary

Solution
1) Create dictionary and sliding window l and r
2) use r for iteration and l for remembering left side of window/substring
3) update current string len and character to dictionary
4) Check if the window has valid string by check curr_len with max_freq_in_dict + k
    this makes sense coz the k can only replcae minority values and both addedd should be less than curr_len
5) If the window legit update res if needed
6) if the winow not legit decrement dictionary count of left pointer and increment its window position

"""



class Solution:
    def characterReplacement(self, s, k):
        l = 0
        res =  0
        freq = {} # Frequency of characters
        for r,char in enumerate(s):
            curr_len = r-l+1   # calculate length of curre string
            freq[char] = 1 + freq.get(char,0) # add current element to the dictionary
       
            # if k and max_char_value can make the curernt lenght 
            # then its good string where chracter can be exchanged
            if curr_len <=  max(freq.values()) + k:
                if curr_len>res:
                    res = curr_len
            # if the sting miniority can be replced by k then remove the last element in sliding window
            else: 
                # remove the last element in window and update l pointer
                freq[s[l]] -= 1 
                l+=1
        
                   
            
        return res

