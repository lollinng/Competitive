class Solution():

    def __init__(self):
        pass
    def run(self):
        pass

inputs = int(input())
for i in range(inputs):
    peeps = int(input())

    people_time = input().split()
    for i in range(peeps):
        people_time[i] = int(people_time[i])

    people_pos = input().split()
    for i in range(peeps):
        people_pos[i] = int(people_pos[i])


    obj = Solution(peeps,people_time,people_pos)
    print(obj.run())