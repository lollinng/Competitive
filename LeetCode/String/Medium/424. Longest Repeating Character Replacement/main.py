class Solution:
    def characterReplacement(self, s, k):
        
        '''

        2 pointer approach to allow k different 

        variable calculating difference

        AABABBA  k =1

        AABA res=4
        AABAB  False , hence loop over from left till we reach curr_len = max_value+k
        BAB
        BABB answer 4 
        BABBA wrong hence loop over from left
        BBA
        

        '''
        string_len = len(s)

        left = 0
        value_counter = {}
        most_freq_char = 0
        for right in range(string_len):
            ele = s[right]

            value_counter[ele] = value_counter.get(ele,0) + 1
            most_freq_char = max(most_freq_char,value_counter[ele])


            if (right-left+1) - most_freq_char > k:
                value_counter[s[left]]-=1
                left+=1
        
        return right-left+1
                
