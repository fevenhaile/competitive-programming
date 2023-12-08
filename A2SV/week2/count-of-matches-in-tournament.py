class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalmatches = 0
        teams_advancing = 0

        while n > 1:
            if n % 2 == 0:
                matches = n // 2
                teams_advancing = matches
                totalmatches += matches
            else:
                matches = (n - 1) // 2
                teams_advancing = matches + 1
                totalmatches += matches
            n = teams_advancing

        return totalmatches