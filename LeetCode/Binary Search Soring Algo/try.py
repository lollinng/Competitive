
def binary_search(arr,num):
    r = len(arr)-1
    l = 0

    while(l<=r):

        # calc mid
        mid = l+(r-l+1)//2
        
        # check if condition satisfied
        if arr[mid] == num:
            return mid
        # select sublist
        elif arr[mid] > num:
            r = r-1
        else:
            l= l+1

    return mid

arr = [1,3,5,7,9,10]
print(binary_search(arr,4))