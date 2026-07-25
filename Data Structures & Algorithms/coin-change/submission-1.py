from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(amt):
            if amt == 0:
                return 0 
            if amt<0:
                return float('inf')
            ans = float('inf')
            for nums in coins:
                ans = min(ans,1+dfs(amt-nums))
            return ans
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res