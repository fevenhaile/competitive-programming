class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        SameRowWords = []

        for word in words:
            if all(char.lower() in row1 for char in word):
                SameRowWords.append(word)
            elif all(char.lower() in row2 for char in word):
                SameRowWords.append(word)
            elif all(char.lower() in row3 for char in word):
                SameRowWords.append(word)

        return SameRowWords