class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[]]
            return
            
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.prefix[r - 1][c]
                    + self.prefix[r][c - 1]
                    - self.prefix[r - 1][c - 1]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.prefix[r2 + 1][c2 + 1]
            - self.prefix[r2 + 1][c1]
            - self.prefix[r1][c2 + 1]
            + self.prefix[r1][c1]
        )