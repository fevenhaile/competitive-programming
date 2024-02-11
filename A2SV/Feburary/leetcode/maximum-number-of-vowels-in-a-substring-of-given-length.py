class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vcounter = 0
        maxim = 0
        
        
        
        l = 0
        r = 0

        while r < len(s):
            if s[r] in vowels:
                vcounter += 1
            
            if r - l + 1 > k:
                if s[l] in vowels:
                    vcounter -= 1
                l += 1
            
            maxim = max(maxim, vcounter)
            r += 1
                
        return maxim