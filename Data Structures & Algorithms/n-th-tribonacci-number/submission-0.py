from functools import lru_cache
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = []
        @lru_cache(maxsize=32)
        def fib(k):
            if k == 1 or k ==2:
                return 1
            if k == 0:
                return 0
            
            return fib(k-1)+fib(k-2)+fib(k-3)
        return fib(n)
            
