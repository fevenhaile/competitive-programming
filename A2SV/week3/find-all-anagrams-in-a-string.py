class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dicp = Counter(p)
        if len(p) > len(s):
            return []
        dics = Counter(s[:len(p)])
        ans = []
        
        for i in range(len(s)-len(p)):
            if dicp == dics:
                ans.append(i)
            dics[s[i]] -= 1
            dics[s[i+len(p)]] += 1
        if dicp == dics:
            ans.append(len(s)-len(p))
        return ans

        
                
            


        
            


        
        