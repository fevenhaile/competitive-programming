class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word3 = ""
        word4 = ""
        
        for i in range(len(word1)):
            word3 += word1[i]
        
        for i in range(len(word2)):
            word4 += word2[i]

        if word3 == word4:
            return True
        