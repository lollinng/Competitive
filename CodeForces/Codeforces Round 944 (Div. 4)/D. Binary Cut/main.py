"""
if we start 
with 
1 : got till it reaches 0 , dont take the zero with it 
0 : go till it reaches 1 take the one with it

possible scense


0->0 - continue
0->1 - continue
1->0 - wrong add res 
1->1 - continue

The beauty is 01 can only happen once damnn
next time 01 will cost you

"""


def run(chars):
    res = 0 
    n = len(chars)
    i = 1
    one_zero_one = True
    last_char = chars[0]
    while(i<n):
        # if last char is 0
        if last_char == '0':
            if chars[i] != '0' :
                if one_zero_one:
                    one_zero_one = False
                else:
                    res+=1
                last_char = '1'
                
            
               
        # if last char is 1
        else:
            if chars[i] != '1':
                res+=1
                last_char='0'
        i+=1   

    return res+1




loop = int(input())
for _ in range(loop):
    print(run(input()))