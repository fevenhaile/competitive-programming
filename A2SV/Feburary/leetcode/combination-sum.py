class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        comb = []
        candidates.sort()
        def backtrack(j):
            if sum(comb) == target:
                ans.append(comb[:])
                return
            if sum(comb) > target:
                return 
            

            for i in range(j,len(candidates)):
                comb.append(candidates[i])
                backtrack(i)
                comb.pop()
            
                
        backtrack(0)
        return ans
        

        

