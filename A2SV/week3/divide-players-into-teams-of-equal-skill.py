class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result  = []
        l = 0
        r = len(skill) - 1
        while l <= r:
            if skill[l] + skill[r] == skill[l+1] + skill[r-1]:
                result.append((skill[l],skill[r]))
                l += 1
                r -= 1
                
            else:
                return -1
        x = 0
        for i in range(len(result)):
            x += result[i][0]*result[i][1]
        return x