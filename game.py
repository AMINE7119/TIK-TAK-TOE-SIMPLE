from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.playerX = Player('X')
        self.playerO = Player('O')
        self.curr_player = self.playerX
        self.turns = 0
        self.game_over = False

    def switch_player(self):
        """Switch the current player."""
        self.curr_player = self.playerX if self.curr_player == self.playerO else self.playerO

    def make_move(self, row, col, piece_size):
        """Handle a move by the current player."""
        if self.game_over:
            return False

        if self.board.is_empty(row, col) and self.curr_player.use_piece(piece_size):
            self.board.place_piece(row, col, piece_size)
            return True
        elif self.board.can_take_over(row, col, piece_size):
            self.board.replace_piece(row, col, piece_size)
            return True
        return False

    def check_winner(self):
        result = self.board.check_winner()
        if result == "Tie":
            self.game_over = True
            return "Tie!"
        if result:
            self.game_over = True
            return f"{self.curr_player.name} wins!"
        return None

    def reset_game(self):
        self.board.reset()
        self.turns = 0
        self.game_over = False
        self.playerX.pieces = {'small': 3, 'medium': 3, 'large': 3}
        self.playerO.pieces = {'small': 3, 'medium': 3, 'large': 3}
        self.curr_player = self.playerX
