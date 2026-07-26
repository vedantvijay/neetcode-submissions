from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(s,i):
            if i in memo:
                return memo[i]
            if i >=len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            ans = dfs(s,i+1)
            if int(s[i:i+2])<=26 and int(s[i:i+2])>=10:
                ans += dfs(s,i+2)
            memo[i] = ans
            return memo[i]
        return dfs(s,0)
            
            