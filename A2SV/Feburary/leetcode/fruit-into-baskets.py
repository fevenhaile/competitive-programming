class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = 0
        l = 0
        r = 0
        maxim = 0
        window = {}

        while r < len(fruits):
            window[fruits[r]] = window.get(fruits[r], 0) + 1
            count += 1

            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
                count -= 1

            maxim = max(maxim, count)
            r += 1

        return maxim