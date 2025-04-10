# minimax.py
import chess
from evaluation import evaluate_board

def minimax(board: chess.Board, depth: int, maximizing: bool) -> (float, chess.Move):
    """
    Minimax algorithm without alpha-beta pruning.
    Returns a tuple: (score, best_move)
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    
    if maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        return min_eval, best_move

# Example usage:
if __name__ == '__main__':
    board = chess.Board()
    score, move = minimax(board, depth=3, maximizing=True)
    print("Best Move:", move, "with evaluation:", score)
