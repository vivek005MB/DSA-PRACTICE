class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.method1(n) 
    
    def method1(self,n):
        count = 0
        
        for i in range(32):
            cond = n & (1 << i)
            # print(cond)
            if cond != 0:
                count +=1 
        return count
            
        