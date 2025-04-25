import os
import time
import chess
from minimax import minimax
from alphabeta import alphabeta
from video_creator import board_to_image_with_overlay, create_game_video

def play_and_record(depth: int = 3,
                    fps: int = 1,
                    delay: float = 0.5,
                    output_filename: str = 'game_video.mp4'):
    """
    Plays a full chess game (White=Minimax, Black=Alpha-Beta), snapshots each position
    with FEN+move annotation, then compiles into an MP4.
    """
    board = chess.Board()
    snapshots = []
    os.makedirs('snapshots', exist_ok=True)

    print("Starting recorded game between Minimax (White) and Alpha-Beta (Black)\n")
    move_number = 1

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            score, move = minimax(board, depth, True)
            algo = "Minimax"
            player = "White"
        else:
            score, move = alphabeta(board, depth, float('-inf'), float('inf'), False)
            algo = "Alpha-Beta"
            player = "Black"

        if move is None:
            print("No legal moves available.")
            break

        fen = board.fen()
        annotation = [
            f"FEN: {fen}",
            f"{player} using {algo} chose move: {move.uci()} (eval: {score:.2f})"
        ]
        board.push(move)

        idx = len(snapshots) + 1
        img_path = f'snapshots/{idx:03d}_{player[0]}{move.uci()}.png'
        board_to_image_with_overlay(board, annotation, img_path)
        snapshots.append(img_path)

        print(f"{player} {algo} → {move.uci()} (eval {score:.2f})")
        time.sleep(delay)
        move_number += 1

    print("Game over! Result:", board.result())
    print(f"Compiling {len(snapshots)} frames into {output_filename} at {fps}fps…")
    create_game_video(snapshots, output_filename=output_filename, fps=fps)
    print("Video saved to", output_filename)


if __name__ == "__main__":
    play_and_record(depth=3, fps=1, delay=0.5, output_filename='game_video.mp4')
