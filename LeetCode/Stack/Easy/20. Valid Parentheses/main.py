class Solution:
    def isValid(self, s):
        if len(s)<2:
            return False

        chars = []
        dict_ ={
            '(':')',
            '[':']',
            '{':'}'
        }


        for i in s:
            if i not in dict_:
                if chars==[]:
                    return False
                if i != chars[-1]:
                    return False
                chars.pop()
            else:
                chars.append(dict_[i])
        return True if chars == [] else False