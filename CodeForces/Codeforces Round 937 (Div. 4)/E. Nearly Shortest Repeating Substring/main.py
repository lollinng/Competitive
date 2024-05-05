'''

find substring such that upon repeating multiple times till length of the string
it only has one or no different characters

Intuition
1) Lets use brute force and iterate throught the array to check
validation from different substring

How to check if string is same or one difference in character


'''


# def valid(main_str,temp_str,n):
#     cnt = 0
#     for i in range(n):
#         if main_str[i] != temp_str[i]:
#             cnt+=1
#         if cnt>1:
#             return False
#     return True

# def calculate(n,characters):
#     res = float('+inf')
#     for i in range(n):
#         for j in range(i+1,n+1):
#             temp = ''
 
#             if len(characters[i:j]) > n//2:
#                 j==n+1
 
#             while True:
#                 temp += characters[i:j]
#                 if len(temp) == n and valid(characters,temp,n):
#                     res = min(res,len(characters[i:j]))
#                     break
#                 elif len(temp) > n:
#                     break
#     return res

# k = int(input())
# for _ in range(k):
#     n = int(input())
#     print(calculate(n,input()))


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    # Iterate through possible lengths of k
     
        
        if valid:
            print(length)
            break