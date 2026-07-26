from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        @lru_cache(maxsize=None)
        def dfs(s,i):
            if i >=len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            ans = dfs(s,i+1)
            if int(s[i:i+2])<=26 and int(s[i:i+2])>=10:
                ans += dfs(s,i+2)
            return ans 
        return dfs(s,0)
            
            