from functools import lru_cache
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def fib(k):
            if k == 1 or k ==2:
                return 1
            if k == 0:
                return 0
            if k not in memo:
                memo[k]=(fib(k-1)+fib(k-2)+fib(k-3))
            return memo[k]
        return fib(n)
            
