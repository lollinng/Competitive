class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(),happiness.end(),greater<int>());
        /*
        [21,5,6,5,4,3,2]
        k = 3
        21 - 0   ,  i = 0
        6 - 1    ,  i = 1 k = 3
        5 - 2     , i = 2 , k = 3

        4 - 3     , i=3,k=3



        */  
        long long res = 0; 
        for (int i=0;i<k;i++){
            res += max(happiness[i]-i,0);        
        }     
        return res;
    }
};