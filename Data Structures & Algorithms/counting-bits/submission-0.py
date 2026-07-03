class Solution:
    def countBits(self, n: int) -> List[int]:
        listy = []
        for i in range(n+1):
            x = bin(i)[2:]
            listy.append(x.count("1"))
        return listy