class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        valid_c = [0] 
        
        for i in range(1, len(s) + 1):
            for c in valid_c:
                if s[c:i] in wordDict:
                    valid_c.append(i) 
                    break
        return len(s) in valid_c