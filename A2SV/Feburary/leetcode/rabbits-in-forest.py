class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        dic = Counter(answers)
        for i in dic:
            ans += (ceil( dic[i]/(i+1) ) * (i+1))
        return ans
        