class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [ [0] * len(colSum) for _ in rowSum]
        print(mat)
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                minus =  min(rowSum[i],colSum[j])
                mat[i][j] = minus
                rowSum[i] -= minus
                colSum[j] -= minus
        return mat