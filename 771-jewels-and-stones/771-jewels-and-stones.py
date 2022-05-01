class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return self.method1(jewels,stones)
    
    def method1(self,jewels,stones):
        keys = set()
        for char in jewels:
            keys.add(char)
        count = 0
        for char in stones:
            if char in keys:
                count += 1
        return count
        
            
            