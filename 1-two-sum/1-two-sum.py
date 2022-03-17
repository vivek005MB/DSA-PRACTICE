class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.method3(nums,target)
    
    
    def method1(nums,tarrget):
        for i in range(len(nums)-1):
            rem = target - nums[i]
            if rem in nums[i+1:]:
                j = nums[i+1:].index(rem)
        return list((i,j+i+1))
    
    def method2(self,nums,target):
        d ={}
        rem = 0
        for idx,val in enumerate(nums):
            d[val]=idx
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d and d[rem] != i:
                return (i,d[rem])
    def method3(self,nums,target):
        visited={}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in visited:
                return [visited[target-nums[i]],i]
            visited[nums[i]] = i
            
        
            
            

        
        