class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False