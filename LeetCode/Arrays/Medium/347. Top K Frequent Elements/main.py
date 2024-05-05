'''
return k most frequent elements
doesnt means elements with atleast k frequency
it means elements which are top k frequent, means top1 frequence top2 frequent and top k frequent
'''

class Solution:
    def topKFrequent(self, nums):
        
        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        # sort array in decending order of values
        freq = dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        return list(freq.keys())[:k]
        

        # x = Counter(nums)
        # x = x.most_common(k)
        # return [i[0] for i in x]
       