class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        numbertrue = 0
        numberfalse = 0
        ans = 0
        for right in range(len(answerKey)):
            
            if answerKey[right] == "T":
                numbertrue+=1

            else:
                numberfalse+=1

            while numberfalse > k and numbertrue > k:
                if answerKey[left] == "T":
                    numbertrue -= 1
                else:
                    numberfalse -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans