class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        dic = defaultdict(int)
        maxim = 0
        
        for r in range(len(s)):
            
            dic[s[r]] += 1
            while sum(dic.values()) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l+=1
            maxim = max(maxim,sum(dic.values()))
        return maxim






        