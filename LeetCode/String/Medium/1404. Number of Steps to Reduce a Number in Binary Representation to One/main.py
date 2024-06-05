class Solution:
    def numSteps(self, s):

        def addOne(s):
            i = len(s) - 1
            str_list = list(s)
            while(i!=-1):
                if str_list[i]=='0':
                    str_list[i]='1'
                    return "".join(str_list)
                else:
                    str_list[i] = '0'
                i-=1
            
            return '1' + "".join(str_list)
            


        steps = 0
        while (s!='1'):
            if s[-1]=='0':
                s = s[:-1]  # dividing by 2
            else:
                s = addOne(s)
            steps+=1
        return steps
        