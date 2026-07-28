from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i,j):
            if i >= len(nums):
                return 0  
            include = dfs(i+1,j)
            if j== -1 or nums[j]<nums[i]:
                include = max(include,1+dfs(i+1,i))
            return include
        return dfs(0,-1)