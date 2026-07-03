class Solution:

    def encode(self, strs: List[str]) -> str:
        su = ""
        for i in strs:
            su = su + "x^x"+ i
        return su
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res1 = s[3:].split("x^x")
        return res1