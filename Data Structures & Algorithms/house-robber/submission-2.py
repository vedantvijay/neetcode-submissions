class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def solve(nums,i):
            if i>=len(nums):
                return 0
            if i not in memo:
                rob = nums[i]+solve(nums,i+2)
                skip = solve(nums,i+1)
                memo[i] = max(rob,skip)
            return memo[i]
        return solve(nums,0)

        