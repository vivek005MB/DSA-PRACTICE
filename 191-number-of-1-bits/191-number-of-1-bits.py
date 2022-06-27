class Solution:
    def hammingWeight(self, n: int) -> int:
        # return self.method1(n) 
        return self.method2(n)
    
    def method1(self,n):
        '''
        using bit manipulation techinique and iterating over all digits of 
        given number we can count number of 1's
        logic : n & (1 << i)
        '''
        count = 0
        
        for i in range(32):
            cond = n & (1 << i)  
            if cond != 0:
                count +=1 
        return count
    
    def method2(self,n):
        ''' 
        using bin function to convert the int to binary string
        bin(15) --> 0b1111 , so counting number of 1's after first two 
        digits       
        '''
        return bin(n)[2:].count('1')
            
        