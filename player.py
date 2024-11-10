class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = {'small': 3, 'medium': 3, 'large': 3}

    def use_piece(self, piece_size):
        """Decrease the number of pieces of the given size."""
        if self.pieces.get(piece_size) > 0:
            self.pieces[piece_size] -= 1
            return True
        return False

    def get_piece_count(self):
        """Return a dictionary of remaining pieces."""
        return self.pieces
