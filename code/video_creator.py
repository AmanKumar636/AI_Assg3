# video_creator.py (Optional)
import chess
import chess.svg
import cairosvg
from moviepy.editor import ImageSequenceClip

def board_to_image(board, filename='temp.png'):
    # Render board as SVG and convert to PNG using cairosvg
    svg_data = chess.svg.board(board=board)
    cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to=filename)

def create_game_video(image_files, output_filename='game_video.mp4', fps=1):
    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_filename)

# Inside your game loop, store images after each move:
# image_files = []
# for move in game_moves:
#     board.push(move)
#     filename = f"images/{move.uci()}.png"
#     board_to_image(board, filename)
#     image_files.append(filename)
# create_game_video(image_files)
