def calculate(time_str):
    res = int(time_str[:2])
    if res>=12:
        res = res-12
        pred = ' PM'
    else: 
        pred = ' AM'

    if res==0:
        res = 12
    elif res <10:
        res = '0'+str(res)    
    
    return str(res)+time_str[2:5]+pred
    


k = int(input())
for _ in range(k):
    print(calculate(input()))