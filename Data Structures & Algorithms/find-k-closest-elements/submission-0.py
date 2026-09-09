class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = []
        res = []
        for i in arr:
            new_arr.append([abs(i-x),i])
        new_arr.sort()
        for j in range(k):
            res.append(new_arr[j][1])
        res.sort()
        return res

        
        
