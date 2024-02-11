class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        r = 0
        maxlength = 0
        
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                maxlength = max(maxlength,len(unique))
                r += 1
                print(unique)
            else:
                unique.remove(s[l])
                l += 1
                
        return maxlength



        