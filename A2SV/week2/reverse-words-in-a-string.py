class Solution:
    def reverseWords(self, s: str) -> str:
        values = s.split()
        answer = list(values[::-1])
        return ' '.join(answer)
        
        
       

        