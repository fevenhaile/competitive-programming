class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lett = []
        newval = []
        visited = set()
        
        def backtrack(row, col, idx):
            if idx == len(word):
                return True
                
            if not(0 <= row < len(board) and 0 <= col < len(board[0])):
                return False
            if (row, col) in visited:
                return False
            if word[idx] != board[row][col]:
                return False

            visited.add((row, col))
            if backtrack(row+1,col, idx + 1):
                return True
            if backtrack(row-1,col, idx + 1):
                return True
            if backtrack(row,col+1, idx + 1):
                return True
            if backtrack(row,col-1, idx + 1):
                return True
            # how to go in the four directions
            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
