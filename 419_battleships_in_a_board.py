class Solution:
    def dfs(self, board, i, j):
        if (i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == "X"):
            board[i][j] = '.'
            self.dfs(board, i, j+1)
            self.dfs(board, i+1, j)
            return 1
        return 0
        
        
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        retval = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                retval += self.dfs(board, i, j)
        return retval