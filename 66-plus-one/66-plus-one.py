class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.method1(digits)
    def method1(self,nums):
        n = len(nums)
        number = 0
        for i in range(n):
            a = nums.pop()
            number += a * (10**i)
        print(number)
        number+=1
        lis = []
        while(number > 0):
            lis.append(number%10)
            number = number // 10
        return lis[::-1]
        