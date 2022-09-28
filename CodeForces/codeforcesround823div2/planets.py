class Solution:

    def __init__(self,no_planets,power_2,planet_list):
        self.no_planets = no_planets
        self.power_2 = power_2
        self.power_1 = 1
        planet_list.sort()
        self.planet_list = planet_list 

    def run(self):
        # print(self.planet_list)
        divided = []
        temp_score = 0 
        temp = self.planet_list[0]
        for i in self.planet_list:
            if i == temp:
                temp_score +=1
            else:
                divided += [temp_score]
                temp_score = 1
                temp = i
        divided += [temp_score]            

        res = 0
        for i in divided:
            if self.power_1*i>self.power_2:
                res+=self.power_2
            else:
                res+=self.power_1*i

        return res




inputs = int(input())
answer = []
for i in range(inputs):
    planet_list = []

    line = input().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    no_planets, power_2 = line

    planet_list = input().split()
    for i in range(no_planets):
        planet_list[i] = int(planet_list[i])
    obj = Solution(no_planets,power_2,planet_list)
    print(obj.run())



# obj = Solution(10,1,[2,1,4,5,2,4,5,5,1,2])
# print(obj.run())

# obj = Solution(5,2,[3,2,1,2,2])
# print(obj.run())

# obj = Solution(2,2,[1,1])
# print(obj.run())

# obj = Solution(2,2,[1,2])
# print(obj.run())

# obj = Solution(1,100,[1])
# print(obj.run())