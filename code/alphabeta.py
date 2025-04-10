# alphabeta.py
import chess
from evaluation import evaluate_board

def alphabeta(board: chess.Board, depth: int, alpha: float, beta: float, maximizing: bool) -> (float, chess.Move):
    """
    Alpha-Beta pruning algorithm.
    Returns a tuple: (score, best_move)
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    
    if maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval, best_move

# Example usage:
if __name__ == '__main__':
    board = chess.Board()
    score, move = alphabeta(board, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing=True)
    print("Best Move:", move, "with evaluation:", score)
