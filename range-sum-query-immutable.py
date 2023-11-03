class NumArray(object):

    def __init__(self, nums):
        self.prefixsum=[]
        counter=0
        for i in nums:
            counter+=i
            self.prefixsum.append(counter)
        

    def sumRange(self, left, right):
        rightsum=self.prefixsum[right]
        leftsum=self.prefixsum[left-1] if left>0 else 0
        return rightsum-leftsum        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)