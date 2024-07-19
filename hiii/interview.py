'''
(()())


(())())(

{([)]}

curly = 0
square = 0 
circle = 0 
recent = '['
'''

s = '{([])}'
curly= 0
square = 0 
circle = 0 
recent = ''

# diction = ['()']

for i in s:
    if i=='(':
        recent = '('
        circle+=1
    elif i=='{':
        recent = '{'
        curly+=1
    elif i=='[':
        recent = '['
        square+=1

    elif i==')':
        circle-=1
        if circle<0:
            print(False)
            exit(0)
    elif i=='}':
        if recent !='{':
            print(False)
            exit(0)
        curly-=1
    elif i==']':
        if recent !='[':
            print(False)
            exit(0)
        square-=1

if (circle,curly,square == 0,0,0):
    print(True)
else:
    print(False)
    



    




