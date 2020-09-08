class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n
        value = 1 if player == 1 else -1
        
        self.row[row] += value
        self.col[col] += value
        if row == col:
            self.diag += value
        if row == n-col-1:
            self.anti_diag += value

        if n in [self.row[row], self.col[col], self.diag , self.anti_diag]:
            return 1
        elif -n in [self.row[row], self.col[col], self.diag , self.anti_diag]:
            return 2
        else:
            return 0
