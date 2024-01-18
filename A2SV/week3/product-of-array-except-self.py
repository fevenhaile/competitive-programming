class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = []
        ans = []
        x = 1
        y = 1
        # prefis product
        for i in range(len(nums)):
            x *= nums[i]
            prefix.append(x)
        # postfix product
        for i in range(len(nums)-1,-1,-1):
            y *= nums[i]
            postfix.append(y)
        postfix = postfix[::-1]
        postfix.append(1) 
        
        for i in range(len(nums)):
            ans.append(prefix[i] *postfix[i+1])
        return ans
    



