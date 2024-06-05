class Solution:
    def maximumEnergy(self, energy, k):
        
        '''
        Using dp array to store lowest way to get at each index
        we have to return max_enery

        [5,2,-10,-5,1]
        k = 3
        now dp_arr = [5,-inf,-inf,-inf,-inf]

        after first iteration
        check  -k element exist:
            if yes : temp = energy[i-k]
            else: temp=-inf
        dp_arr[1] = res(max(energy[i],energy[i]+temp))
        dp_arr = [5,2,-inf,-inf,-inf]

        dp_arr = [5,2,-10,-inf,-inf]
        dp_arr = [5,2,-10,0,-inf]   # here max(-5,5+-5)
        dp_arr = [5,2,-10,0,3]   # here max(1,1+2)

        return max(dp_arr[:-k]) # last elements which can make jump out of it
        which means max(-10,0,3) = 3
        '''
        n = len(energy)
        dp_array = []*(n-1)

        dp_array.insert(0,energy[0]) 

        i = 1
        while(i<n):
            while(i<k):
                dp_array.insert(i,energy[i])   
                i+=1

            if i ==n:
                break

            res = max(energy[i],energy[i] + dp_array[i-k])
            
            # print(res)
            dp_array.insert(i,res)
            # print(energy[i],dp_array[i-k],res,i,dp_array)
            
            i+=1
        print(dp_array) 
        return max(dp_array[-1:-k-1:-1])


obj  =Solution()
k = [[[5,2,-10,-5,1],3],[ [-2,-3,-1],2]]
k.append([[1],1])
k.append([[1,-10],2])
k.append([[1,-10],1])
k.append([[1,-10,2],1])
# k.append(['bacd','bacd'])

for i in k:
    print(obj.maximumEnergy(i[0],i[1]))