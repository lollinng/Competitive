

def run(chars):
    n = len(chars)
    if n==1:
        print("NO")
        return
    
    x = chars[0]
    for i in range(1,n):
        curr =  chars[i]
        if x !=curr:
            print("YES")
            if i!=n-1:
                print(curr+chars[:i]+chars[i+1:n])
            else:
                print(curr+chars[:i])
            return
    print('NO')

    

loop = int(input())
for _ in range(loop):
    chars = input()
    run(chars)