class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(map(int, sorted(set(nums))))

        return len(nums)