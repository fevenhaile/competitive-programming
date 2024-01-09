class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        words=list(words)

        
        words.sort(key=lambda x : int(x[-1]))
        for i in  range(len(words)):
            words[i]=words[i][:-1]
                    #chaning the list in to a string
            result = ' '.join(words)
        return result
        