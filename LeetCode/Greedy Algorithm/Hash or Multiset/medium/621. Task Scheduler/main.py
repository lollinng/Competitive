'''
Here we are trying to find the time required to process all task give same tasks take n time to refress before
processing again

Intuition -
1) We understand the max recurring task should start at left and we should divide code into chunks of n+1 s.t
we can repeat the max recurring task
for eg - {A:6,B:4,C:2} n = 2
# final o/p will be
# slot size / cycle size = 3
# Number of rows = number of A's (most freq element)
[
    [A, B,      C],
    [A, B,      C],
    [A, B,      idle],
    [A, B,      idle],
    [A, idle,   idle],
    [A   -        - ],     --> max_freq_ele_count
]
2) here we can see that max element comes n times and the slots n+1 is filled n-1 times
so till second_last positon above will o/p (max_freq - 1) * (n+1)
3) now in nth cycle of n+1 we add max_freq_ele_count to the o/p so that if multiple max element
we add them to the o/p as they will be present instead of '-' in above figure
4) there is also an edge case when max element aint big enough as compared to lenght of task hence the
max element can be used without creating an idle time . for that case we add max(ans, len(tasks))
as output

'''


import collections


class Solution:
    def leastInterval(self, tasks, n):

        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freqs = list(freq.values())
        # print(freq, max_freq, freq, freqs)
        # total_elements_with_max_freq, last row elements
        max_freq_ele_count = 0
        i = 0
        while(i < len(freqs)):
            if freqs[i] == max_freq:
                max_freq_ele_count += 1
            i += 1
        print(max_freq_ele_count)

        ans = (max_freq - 1) * (n+1) + max_freq_ele_count

        # in case the len is big enough to run the machine without idle wait time
        return max(ans, len(tasks))


tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
obj = Solution()
print(obj.leastInterval(tasks, n))
