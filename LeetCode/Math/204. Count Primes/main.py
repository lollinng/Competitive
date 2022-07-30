class Solution:
    def countPrimes(self, n):
        # coz it said less than n so,less than 2 is none
        if n < 3:
            return 0

        primes = [True]*n
        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5)+1):
            # multiplying primes with different digits in till range n to fill all composites
            if primes[i]:
                # here j = i*i ,i*2i , i*3i ... till xi=n
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)


obj = Solution()
print(obj.countPrimes(10))
