class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > j and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1)
                comb.pop()
        backtrack(0)
        
        realans = []
        for i in range(len(ans)):
            if ans[i] not in realans:
                realans.append(ans[i])
        
        return realans
