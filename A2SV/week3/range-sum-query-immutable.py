class NumArray:

    def __init__(self, nums: List[int]):
        self.x = 0
        self.prefix = [0]
        self.nums = nums
        for i in range(len(self.nums)):
            self.x += self.nums[i]
            self.prefix.append(self.x)
            
        
        
        

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        return (self.prefix[self.right+1] - self.prefix[self.left])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)