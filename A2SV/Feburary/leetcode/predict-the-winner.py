class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def win(l, r, player1):
            if player1:
                if l == r:
                    return nums[l]
                left = win(l+1, r, not player1) + nums[l]
                right = win(l, r-1, not player1) + nums[r]
                return max(left, right)
            else:
                if l == r:
                    return nums[l]
                left = win(l+1, r, not player1) - nums[l]
                right = win(l, r-1, not player1) - nums[r]
                return min(left, right)
        return win(0, len(nums)-1, True) >= 0