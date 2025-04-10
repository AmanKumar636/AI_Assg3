# evaluation.py
import chess

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # The king is invaluable.
}

def evaluate_board(board: chess.Board) -> float:
    """
    Evaluate a board state based on material count.
    Positive value means advantage for white, negative for black.
    """
    evaluation = 0
    for piece_type in PIECE_VALUES:
        evaluation += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        evaluation -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    return evaluation
