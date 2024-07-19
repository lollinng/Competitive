'''

Longest length of substring with non repeating chars

'abccbad' : 4
'abcabc': 3


0 to 10^5


a b c c b a d

'''




def funcs(s):
    n = len(s)
   
    dict_ = {} 
    pre = 0
    max_length = 0
    temp_length = 0
    for right in range(0,n):

        

        # element is new
        if s[right] not in dict_:
            dict_[s[right]] = right
            temp_length+=1
        # element is already there
        else:
            if pre<dict_[s[right]]:
                pre = dict_[s[right]]

            temp_length = right - pre
            dict_[s[right]] = right

        # print(max_length,temp_length,n,dict_)
        max_length = max(max_length,temp_length)

    return max_length


'''
3 - 2


            a  b c    a  b c d

{
    'a' : 0,
    'b' : 1,
    'c' : 2,  # 3


 }



'''


s = "abbbcdzz"
print(funcs(s))


