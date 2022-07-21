

# 1)   Dynamic Programming top down approach - Uses a top down approch and uses a memory array to store the values of already visited values of n while in recursion

def tribonacci(self, n):
    def recursion(n, memo):
        if(memo[n] != None):
            return memo[n]

        if(n <= 1):
            return n
        if(n == 2):
            return 1
        memo[n] = recursion(n-1, memo)+recursion(n-2,
                                                 memo)+recursion(n-3, memo)
        return memo[n]

    memo = [None]*(n+1)
    return recursion(n, memo)


# 2) Bottom-Up Approach - Here we use a loop to start storing items into array from the left and iterate our
# way to the nth number . Since it doesnt contain any recursion it works better than other approch for big
# values of n

def tribonacci(self, n):
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    array = [None]*(n+1)
    array[0] = 0
    array[1] = array[2] = 1
    for i in range(3, n+1):
        array[i] = array[i-1] + array[i-2] + array[i-3]
    return array[n]
