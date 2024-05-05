1234 + 5678 



x = '3378'
x1 = int(x[2:])
x2 = int(x[:2])

y = '1234'
y1 = int(y[2:])
y2 = int(y[:2])


# x1 = 34 , y1 = 78
going_above_x_50 =False
going_above_Y_50 =False
if x1>50:
    going_above_x_50 = True
    temp_x = x1 - 50
else:  
    temp_x = 50- x1  # this deficiet 16


if y1>50:
    temp_y = y1 - 50  # surplus 28
    going_above_Y_50 =  True
else:
    temp_y = 50- y1




if going_above_Y_50==True and going_above_x_50!=True :
    going_overflow = temp_y - temp_x
if going_above_x_50==True and going_above_Y_50!=True :
    going_overflow = temp_x - temp_y
if going_above_x_50==True and going_above_Y_50==True :
    going_overflow = temp_x + temp_y
if going_above_x_50!=True and going_above_Y_50!=True :
    going_overflow = 0





if going_overflow>0:
    # add over_flow value to other digits
    print(f'adding value {going_overflow} to left side')

    


# print(x1,y1,temp,temp1)

