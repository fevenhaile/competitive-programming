class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join(s.split()) 
        lowecasex = x.lower()

        l = 0
        r = len(lowecasex) - 1
        
        

        while l < r:
            if not lowecasex[l].isalnum():
                l += 1
            elif not lowecasex[r].isalnum():
                r -= 1
            elif r >= 0 and lowecasex[l].isalnum() and lowecasex[r].isalnum():
                if lowecasex[l] == lowecasex[r]:
                    l += 1
                    r -= 1
                else:
                    return False

        return True