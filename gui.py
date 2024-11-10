import tkinter as tk
from game import Game

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)

        self.game = Game()  # Initialize the game
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.window)
        self.label = tk.Label(self.frame, text=f"{self.game.curr_player.name}'s turn", font=("Consolas", 20),
                              background="#343434", foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Canvas for the game board
        self.canvas = tk.Canvas(self.frame, width=300, height=300, bg="lightgray")
        self.canvas.grid(row=1, column=0, columnspan=3)

        # Draw the grid
        self.draw_grid()

        # Buttons to select the piece to play
        self.create_piece_buttons()

        # Store the piece IDs for dragging
        self.piece_images = {}

        self.frame.pack()

    def draw_grid(self):
        """Draw the 3x3 grid on the canvas."""
        # Vertical lines
        for i in range(1, 3):
            self.canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=2)
        
        # Horizontal lines
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=2)

    def create_piece_buttons(self):
        """Create buttons for selecting which piece to play."""
        self.small_button = tk.Button(self.frame, text="Small", command=lambda: self.set_piece('small'))
        self.small_button.grid(row=2, column=0)

        self.medium_button = tk.Button(self.frame, text="Medium", command=lambda: self.set_piece('medium'))
        self.medium_button.grid(row=2, column=1)

        self.large_button = tk.Button(self.frame, text="Large", command=lambda: self.set_piece('large'))
        self.large_button.grid(row=2, column=2)

    def set_piece(self, size):
        """Set the selected piece size."""
        self.dragged_piece = size

    def on_click(self, event):
        """Handle the placement of pieces on the board."""
        if not self.dragged_piece:
            return

        # Calculate the row and column for the click position
        col = event.x // 100
        row = event.y // 100

        if self.game.make_move(row, col, self.dragged_piece):
            self.update_board()
            self.switch_turn()

    def update_board(self):
        """Update the GUI with the current board state."""
        self.canvas.delete("board")
        for row in range(3):
            for col in range(3):
                piece = self.game.board.board[row][col]
                if piece:
                    self.canvas.create_text(col * 100 + 50, row * 100 + 50, text=piece, font=('Arial', 24), tags="board")

    def switch_turn(self):
        """Switch to the next player."""
        self.game.switch_player()
        self.label.config(text=f"{self.game.curr_player.name}'s turn", foreground="white")

    def run(self):
        """Start the main event loop."""
        self.canvas.bind("<Button-1>", self.on_click)
        self.window.mainloop()
