class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # creating a hashmap for row ,column and the 3*3 matrix
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # the squares has a key that consists the 0-3,3-6 and 6-9 index
        squares = collections.defaultdict(set) 

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]:
                   return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j]) 
        return True   


        