class Solution:
    def toLowerCase(self, s: str) -> str:
        ans  ='';
        offset = ord('a') - ord('A')
        for i in s:
            if ord(i) >= ord('A') and ord(i) <= ord('Z'):
                ans += chr(ord(i) + offset)
            else:
                ans += i
        
        return ans
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        