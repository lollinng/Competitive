"""
Here we are trying to find if its possible to drop humans while carpooling at given capacity

inituition - 
1) We create an array of 1001 for len of stops coz all stops betw. 0 <= fromi < toi <= 1000
2) we update the insertion deletion of humans from the car in the stops,using + and - operators
3) we iterate throguh the array adding counter at each value in stop
4) if carload i.e counter gets bigger than capacity we return false else true

Eg - [[2,1,5],[3,3,7]]
stops = [0, 2, 0, 3, 0, -2, 0, -3, 0, 0,...]
here carLoad<=capacity hence its true
"""


class Solution:
    def carPooling(self, trips, capacity):
      # [[2,1,5],[3,3,7]]
        stops = [0]*(1001)
        for t in trips:
            stops[t[1]] += t[0]
            stops[t[2]] -= t[0]
        print(stops[:10])                 # [0, 2, 0, 3, 0, -2, 0, -3, 0, 0]
        carLoad = 0
        for i in range(1001):
            carLoad += stops[i]
            if carLoad > capacity:
                return False
        return True


obj = Solution()
print(obj.carPooling([[2, 1, 5], [3, 3, 7]], 5))
