from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        left = 0
        count = 0
        
        for right in range(len(s2)):
            if s2[right] in freq:
                freq[s2[right]] -= 1
                if freq[s2[right]] >= 0:
                    count += 1
                
            if count == len(s1):
                return True
            
            if right - left + 1 >= len(s1):
                if s2[left] in freq:
                    freq[s2[left]] += 1
                    if freq[s2[left]] > 0:
                        count -= 1
                left += 1
        
        return False