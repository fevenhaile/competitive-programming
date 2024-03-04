class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n + 1 )] 
        ans = []
        comb = []
        def helper(i,comb):
            # base case
            if len(comb) == k:
                ans.append(comb[:])
                return 
            if i >= n:
                return 

            helper(i+1,comb)
            comb.append(nums[i])
            helper(i+1,comb)
            comb.pop()
        helper(0,[])
        return ans
        

    
        