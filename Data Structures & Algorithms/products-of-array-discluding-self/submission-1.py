class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for j in range(len(nums)):
            arr.append(math.prod(nums[j+1:])*math.prod(nums[:j]))            
        return arr