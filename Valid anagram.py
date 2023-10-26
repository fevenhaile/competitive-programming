class Solution(object):
    def isAnagram(self, s, t):
        counter={}

        for char in s:
            if char in counter:
                counter[char]+=1
            else:
                counter[char]=1
        for char in t:
             if char in counter:
                counter[char]-=1
             else:
                 return False
        for val in counter.values():
            if val!=0:
                return False
        return True        

                        