class Solution:
    
    def check_addr(self,addr):
        parts = addr.split('.')

        if len(parts)>4 :
            return False

        for part in parts:
            if len(part)<1 or int(part)>255 or len(part)>1 and part[0]=='0':
                return False
        return True

    def find_address(self,ans,addr,index,dots,s,addr_len):
        
        if dots ==3:
            addr += s[index:addr_len]
            if self.check_addr(addr):
                ans.append(addr)
            return
 
        for next_index in range(index,min(index+3,addr_len)):
            new_addr = addr+s[index:next_index+1]+'.'
            self.find_address(ans,new_addr,next_index+1,dots+1,s,addr_len)

    def restoreIpAddresses(self, s):
        
        addr_len = len(s)
        if addr_len<4 or addr_len>12 or (not s.isdigit()):
            return []

        ans = []
        self.find_address(ans,"",0,0,s,addr_len)
        return ans