# game.py
import chess
import chess.svg
import time
from minimax import minimax
from alphabeta import alphabeta

def play_game(depth: int = 3, delay: float = 1.0):
    board = chess.Board()

    # Decide which algorithm to use for each color:
    # For example: White uses Minimax, Black uses Alpha-Beta
    while not board.is_game_over():
        print(board)
        print("FEN:", board.fen())
        if board.turn == chess.WHITE:
            score, move = minimax(board, depth, maximizing=True)
            algo = "Minimax"
        else:
            score, move = alphabeta(board, depth, alpha=float('-inf'), beta=float('inf'), maximizing=False)
            algo = "Alpha-Beta"
        if move is None:
            print("No legal moves available.")
            break
        print(f"{'White' if board.turn == chess.WHITE else 'Black'} using {algo} chose move: {move} (eval: {score})")
        board.push(move)
        
        # For demonstration, you can render the board to SVG/PNG, save the image, or delay
        # Here we simply wait for a moment.
        time.sleep(delay)
        
    print("Game over!")
    print("Final board position:")
    print(board)
    print("Result:", board.result())

if __name__ == '__main__':
    play_game(depth=3, delay=0.5)
