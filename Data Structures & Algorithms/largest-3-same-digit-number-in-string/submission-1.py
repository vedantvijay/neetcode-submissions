class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = []
        for i in range(len(num)):
            nums.append(num[i])
        my_set = set(num)
        nums = sorted(my_set, reverse=True)
        res = ""
        for i in nums:
            if num.count(i*3) >= 1:
                res = i
                break
        return res*3
        
            
