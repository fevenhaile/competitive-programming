class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]
        unguarded = set()

        wall_set = {(i, j) for i, j in walls}
        guard_set = {(i, j) for i, j in guards}

        for i, j in guards:
            # right
            for c in range(j + 1, n):
                if (i, c) in wall_set or (i, c) in guard_set:
                    break
                unguarded.add((i, c))

            # left
            for c in range(j - 1, -1, -1):
                if (i, c) in wall_set or (i, c) in guard_set:
                    break
                unguarded.add((i, c))

            # up
            for c in range(i - 1, -1, -1):
                if (c, j) in wall_set or (c, j) in guard_set:
                    break
                unguarded.add((c, j))

            # down
            for c in range(i + 1, m):
                if (c, j) in wall_set or (c, j) in guard_set:
                    break
                unguarded.add((c, j))

        return m * n - (len(guards) + len(walls) + len(unguarded))