class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return self.method1(nums)
    def method1(self, nums):
        visited = set()
        res = set() 
        for ele in nums:
            if ele in visited:
                res.add(ele)
            visited.add(ele)
        return list(res)
                