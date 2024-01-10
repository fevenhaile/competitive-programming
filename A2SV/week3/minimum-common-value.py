class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        commonelts = list(nums1.intersection(nums2))
        commonelts.sort()

        if len(commonelts) == 0:
            return -1 
        
        return commonelts[0]