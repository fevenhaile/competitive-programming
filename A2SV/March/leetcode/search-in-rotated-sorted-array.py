class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return -1
        # if len(nums) == 1:
        #     if target == nums[0]:
        #         return 0
        #     else:
        #         return -1
        # if len(nums) == 2:
        #     if target == nums[0]: 
        #         return 0
        #     elif target == nums[1]:
        #         return 1
        #     else:
        #         return -1

            
        # find the pivot index
        l = 0
        h = len(nums) - 1
        pivot = 0
        
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] < nums[h]:
                h = mid
            else:  # Handle the case when nums[mid] == nums[h]
                if nums[l] == nums[mid]:
                    l += 1
                else:
                    h = mid


        # make a binary search
        pivot = l
        l ,h= 0,len(nums)-1
        
        
        while l <= h:
            mid = (l + h) // 2
            realmid = (mid + pivot) % len(nums)
            print(realmid)
            
            if nums[realmid] < target:
                l = mid + 1
            elif nums[realmid] > target:
                h = mid - 1
            elif nums[realmid] == target:
                print(realmid)
                return realmid
            
        return -1