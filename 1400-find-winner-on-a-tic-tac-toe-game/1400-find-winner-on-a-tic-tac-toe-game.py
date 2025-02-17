class Solution(object):
    def check_winner(self, grid):
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
                return grid[i][0]
            if grid[0][i] == grid[1][i] == grid[2][i] != ' ':
                return grid[0][i]
        
        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return grid[0][2]
        
        return None
    
    def tictactoe(self, moves):
        grid = [[' ' for _ in range(3)] for _ in range(3)]

        for i, move in enumerate(moves):
            row, col = move
            grid[row][col] = 'X' if i % 2 == 0 else 'O'

        # Check for a winner after each move
        winner = self.check_winner(grid)
        if winner:
            return "A" if winner == 'X' else "B"

        # Check for pending moves
        if len(moves) < 9:
            return "Pending"
        
        return "Draw"