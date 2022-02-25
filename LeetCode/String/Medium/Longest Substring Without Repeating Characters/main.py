class Solution:
    def lengthOfLongestSubstring(self, s):
        start = max_length = 0
        used_char = {}
        for i, c in enumerate(s):
            # start <= used_char[c] we use this as we dont want our start to decrease and reset to start or smaller number
            # if very past charcter come in contact show in last example 'p'
            if c in used_char and start <= used_char[c]:
                start = used_char[c] + 1
            else:
                # i current index - start moved for not same string + 1 coz arrays start with 0
                max_length = max(max_length, i-start+1)
            used_char[c] = i
            print("start", start)
        return max_length


obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
# print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkep"))
