class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                middle = stack.pop()
                if stack:
                    left = stack[-1]
                    right = i

                    heights = min(height[left],height[right]) - height[middle]
                    width = right - left - 1
                    
                    ans += (heights * width)

            stack.append(i)
        return ans

