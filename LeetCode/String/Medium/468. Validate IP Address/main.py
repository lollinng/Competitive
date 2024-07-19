class Solution:
    
    def check_ipv4(self,queryIP):

        apartsrr = queryIP.split('.')

        if len(parts)!=4:
            return False

        for part in parts:
            if len(val)>3:
                return False
            if len(val)>1 and val[0] == '0':
                return False
            if not val.isdigit() or int(val)>255 or int(val)<0:
                return False
            
        return True

    def _check_hex(self,value):
        
        for char in value:
            if char.isdigit():
                continue
            
            if not(ord('a')<=ord(char)<=ord('f') or ord('A')<=ord(char)<=ord('F')):
                return False
        return True

    def check_ipv6(self,queryIP):
        arr = queryIP.split(':')

        if len(arr)!=8:
            return False

        for val in arr:
       
            if len(val)>4 or len(val)==0:
                return False
            if not self._check_hex(val): 
                return False

        return True
    
    def validIPAddress(self, queryIP: str) -> str:
        
        if self.check_ipv4(queryIP):
            return 'IPv4'
        elif self.check_ipv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'





