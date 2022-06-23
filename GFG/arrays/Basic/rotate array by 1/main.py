def rotate(arr, n):
    right = n-1
    last = arr[n-1]
    while(right != 0):
        arr[right] = arr[right-1]
        right -= 1
    arr[0] = last
    return arr


print(rotate([1, 3, 4, 5, 6], 5))
