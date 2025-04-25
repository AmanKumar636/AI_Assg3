import os
import chess
import chess.svg
import cairosvg
import imageio
from PIL import Image, ImageDraw, ImageFont

def board_to_image_with_overlay(board, annotation_lines, filename='frame.png'):
    """
    Renders the current board (highlighting the last move) to PNG,
    then overlays one or more lines of text (annotation_lines) below it.
    """
    # 1) SVG → PNG of board with last move highlighted
    last_move = board.peek() if board.move_stack else None
    svg = chess.svg.board(
        board=board,
        lastmove=last_move,
        colors={"square light": "#f0d9b5", "square dark": "#b58863"},
    )
    board_png = filename.replace('.png', '_board.png')
    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=board_png)

    # 2) Prepare text overlay
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        font = ImageFont.load_default()

    # estimate line height via font metrics
    try:
        ascent, descent = font.getmetrics()
        line_height = ascent + descent + 4
    except AttributeError:
        # fallback if getmetrics isn't available
        line_height = 18

    overlay_height = line_height * len(annotation_lines) + 10
    overlay_width = 400

    overlay = Image.new("RGB", (overlay_width, overlay_height), "white")
    draw = ImageDraw.Draw(overlay)

    y = 5
    for line in annotation_lines:
        draw.text((5, y), line, font=font, fill="black")
        y += line_height

    # 3) Combine board + overlay
    board_img = Image.open(board_png).resize((400, 400))
    out_img = Image.new("RGB", (400, 400 + overlay_height), "white")
    out_img.paste(board_img, (0, 0))
    out_img.paste(overlay, (0, 400))
    out_img.save(filename)


def create_game_video(image_files, output_filename='game_video.mp4', fps=1):
    """
    Stitches PNG frames into an MP4 using imageio’s ffmpeg plugin.
    Requires: pip install imageio[ffmpeg]
    """
    os.makedirs(os.path.dirname(output_filename) or '.', exist_ok=True)
    with imageio.get_writer(output_filename, fps=fps) as writer:
        for img in image_files:
            frame = imageio.imread(img)
            writer.append_data(frame)
