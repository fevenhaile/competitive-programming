class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        concatenate = ""
        newstring = ""
        

        length = max(len(word1), len(word2))
        
        for i in range(length):
           
            if i < len(word1):
                concatenate += word1[i]
            
            if i < len(word2):
                concatenate += word2[i]
            
            newstring += concatenate
            concatenate = ""
        
        return newstring
                

        