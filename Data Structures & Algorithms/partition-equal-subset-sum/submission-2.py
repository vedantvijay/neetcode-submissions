class Solution:
    def canPartition(self, a: List[int]) -> bool:
        amt = 0
        memo = defaultdict(bool)
        total = sum(a)
        def dfs(i,amt):
            
            if total % 2:
                return False
            target = total // 2
            if (i,amt) in memo:
                return memo[(i,amt)]
            if i>len(a)-1:
                return False
            if amt == target:
                return True
            take = dfs(i+1,amt+a[i])
            skip = dfs(i+1,amt)
            memo[(i,amt)] = take or skip
            print(amt)
            return memo[(i,amt)]

        return(dfs(0,amt))