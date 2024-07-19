'''
Question was an easy/medium one from LC.

Given a string with any format containing only english letters, replace every percent-sign-sorrounded word (%EXAMPLE%) with the corresponding variable given inside a dictionary passed as an argument. Example:

input = "home/usr/lib/%EXAMPLE%", {EXAMPLE: "testfile.tx"}
output =  "home/usr/lib/testfile.txt"

input = "Hi %USER% how are you doing today %DATE%?", {USER: "John", DATE: "01/01/2024"}
output =  "Hi John how are you doing today 01/01/2024?"
My response was a simple algorithm that goes through every letter and whenever I see % I would call another function to get the closing sign. If no closing sign was found or no variable was mapped to that variable name, I would return error

Follow Up Question:

Imagine your dictionary with variables had nested variables. For example:

input = "Hi %USER%", {USER: "%PRONOUN% John", PRONOUN: "Mr."}
My answer was call recursively the original function to get the final string. Interviewer said it was fine but another way was to flatten the variable dictionary before getting to change the original string.
'''


'''

We have to replace word inside %%

now if only 1 % I will return -1


1) iterate over list 
2) When i find % I call another function which loops over till it finds the other percentage
3) If iteration doesn find other percentage I return -1 
4) If found other percentage I will return the derived string

input = "home/usr/lib/%

send remining string EXAMPLE%
and return testfile.tx using {EXAMPLE: "testfile.tx"} 

and output home/usr/lib/testfile.txt"


'''

class Solution:

    def __init__(self,dictionary):
        self.decoder = self.decode_dict(dictionary) 

    def decode_dict(dictionary):

        def resolve_value(value):

            while '%' in value:
                start = value.find('%')
                end = value.find('%',start+1)

                if end==-1:
                    return -1

                decoded_key = value[start+1:end]
                decoded_word = dictionary[decoded_key]
  
                value = value[:start] + decoded_word + value[end+1:]

            return value            
        

        for key in dictionary.keys():
            value = resolve_value(dictionary[key])
            dictionary[key] = value

        return dictionary

    

    def helper(self,left_index,input_str,input_len):
        
        right_index = left_index+1
        while right_index<input_len and input_str[right_index]!='%':
            right_index+=1            
        
        if right_index== input_len:
            return -1,right_index
        
        key = input_str[left_index+1:right_index]

        if key not in self.decoder:
            return -1,right_index
        

        return self.decoder[key],right_index


    def decode_string(self,input_str):
        
        result = []
        input_len = len(input_str)
        i = 0
        while i<input_len:
            if input_str[i]=='%':
                word,index = self.helper(i,input_str,input_len)
                if word==-1:
                    return -1
                result.append(word)
                i=index+1
            else:
                result.append(input_str[i])
                i+=1

        # print(result)
        # return result
        return ''.join(result)

                
input = {"USER": "%PRONOUN% John", "PRONOUN": "Mr."}



                
# Example usage:
decoder = {"EXAMPLE": "testfile.txt", "USER": "John", "DATE": "01/01/2024"}
solution = Solution(decoder)

input_str1 = "home/usr/lib/%EXAMPLE%"
output1 = solution.decode_string(input_str1)
print(output1)  # Output: "home/usr/lib/testfile.txt"

input_str2 = "Hi %USER% how are you doing today %DATE%?"
output2 = solution.decode_string(input_str2)
print(output2)
                

