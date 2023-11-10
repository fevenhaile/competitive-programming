class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left,right = 0,2
        count = 0
        for i in range(2,len(s)):
            print(i)
            if  s[i] != s[i-2] and s[i] != s[i-1] and s[i-1] != s[i-2]:
                count += 1
   
        return count