class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0] 
        
        for i in range(1, len(nums)):
            n = nums[i]
            temp_max = max(n, curMax * n, curMin * n)
            
            curMin = min(n, curMax * n, curMin * n)
            curMax = temp_max
           
            res = max(res, curMax)
            
        return res