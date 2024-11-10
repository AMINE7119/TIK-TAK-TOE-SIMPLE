class Board:
    def __init__(self):
        # 3x3 grid initialized with empty strings
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def is_empty(self, row, col):
        """Check if a cell is empty."""
        return self.board[row][col] == ''

    def can_take_over(self, row, col, piece_size):
        """Check if a piece can take over a smaller piece."""
        if self.board[row][col] == '':
            return False
        current_piece = self.board[row][col]
        if piece_size == 'medium' and current_piece == 'small':
            return True
        if piece_size == 'large' and (current_piece == 'small' or current_piece == 'medium'):
            return True
        return False

    def place_piece(self, row, col, piece_size):
        """Place a piece on the board."""
        self.board[row][col] = piece_size

    def replace_piece(self, row, col, piece_size):
        """Replace a smaller piece with a larger piece."""
        self.board[row][col] = piece_size

    def check_winner(self):
        """Check for a winner or tie."""
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '':
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return True

        # Check for tie
        for row in self.board:
            for cell in row:
                if cell == '':  # Still an empty spot, not a tie
                    return False
        return "Tie"
