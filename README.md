# AI_Assg3 / Chess-Game-Playing-AI

A repository demonstrating AI game playing in Chess using two classic algorithms: **Minimax** and **Alpha‑β Pruning**. The project includes implementations of both algorithms, an evaluation function based on material count, and a game loop that pits the two methods against each other. Additionally, the repository includes scripts to generate game videos and a slide deck to present the results and insights.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Code](#running-the-code)
  - [Game Simulation](#game-simulation)
  - [Video Generation (Optional)](#video-generation-optional)
- [Algorithm Descriptions](#algorithm-descriptions)
  - [Minimax](#minimax)
  - [Alpha Beta Pruning](#alpha-beta-pruning)
- [Evaluation Function](#evaluation-function)
- [Presentation Slides](#presentation-slides)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements two game playing AI algorithms on a Chess environment using the [python-chess](https://python-chess.readthedocs.io/) library. Both **Minimax** and **Alpha‑β Pruning** algorithms are implemented, compared, and evaluated using a simple evaluation function based on material value. The repository includes:

- **Code:** Algorithm implementations and game simulation scripts.
- **Videos:** Recorded game sessions.
- **Slides:** A slide deck (maximum five slides) presenting the project overview, experimental setup, results, and insights.

## Project Structure

```plaintext
Chess-Game-Playing-AI/
├── code/
│   ├── evaluation.py       # Evaluation function for chess board
│   ├── minimax.py          # Implementation of the minimax algorithm
│   ├── alphabeta.py        # Implementation of the alpha-beta pruning algorithm
│   ├── game.py             # Game simulation and loop integrating both algorithms
│   └── video_creator.py    # (Optional) Script to create game videos from board images
├── videos/
│   ├── game_video.mp4      # Example video of a full game session
│   └── additional_game_video.mp4
├── slides/
│   └── Chess_AI_Slides.pdf  # Slide deck presenting the project overview and results
├── requirements.txt        # Required python packages (python-chess, numpy, etc.)
└── README.md               # This README file

```

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Chess-Game-Playing-AI.git
cd Chess-Game-Playing-AI
```

### 2. Create and Activate a Virtual Environment:
```bash
python -m venv env
source env/Scripts/activate   # On Windows
# For Linux/Mac, use: source env/bin/activate
```

### 3.Install Required Packages:
```bash
pip install -r requirements.txt
```

## Running the Code
To help replicate our experiments, follow the instructions below:

## Game Simulation

1. Run the Game Loop:
The game simulation script pits the two algorithms against each other in a chess game. White uses the Minimax algorithm, and Black uses the Alpha‑β Pruning algorithm. To run the simulation:

```bash
python code/game.py
```

* The script displays the chess board in text format.
* It prints out each move along with the evaluation score.
* The game continues until a game-over condition (checkmate, stalemate, etc.) is reached.

2. Adjusting Parameters:
* Depth: You can adjust the search depth for the algorithms within the game.py file by modifying the depth parameter.
* Delay: Modify the delay between moves (in seconds) by changing the delay parameter in the call to play_game(). This is useful if you want to slow down the simulation for demonstration purposes.

### Video Generation (Optional)
If you want to generate a video from the board states during gameplay:

1. Modifying the Game Loop for Image Capture:
   * Update game.py to save a board image after each move using the helper function from video_creator.py.
   * For instance, within the game loop, after board.push(move), call a function to save the board state as an image (e.g., board_to_image(board, filename)).

2. Generate the Video:
   Once you have a series of image files (saved to a folder such as images/), generate a video using:

   ```bash
   python code/video_creator.py
  

This script will compile the image sequence into a video (e.g., game_video.mp4) and save it to the videos/ folder.

## Algorithm Descriptions

### Minimax
The Minimax algorithm is implemented recursively to search the game tree up to a fixed depth. It evaluates moves using the evaluation function (material difference) to choose the optimal move for the maximizing player (White) and the minimizing player (Black).

### Alpha Beta Pruning
Alpha‑β Pruning enhances the basic minimax algorithm by pruning search tree branches that cannot influence the decision. This improves computational efficiency while ensuring that the optimal move is still selected.

## Evaluation Function
The evaluation function assesses the chess board using a simple material-count method:

* Pawn: 1 point
* Knight/Bishop: 3 points each
* Rook: 5 points
* Queen: 9 points
* King: Invaluable (treated as 0)

A positive score indicates an advantage for White, while a negative score indicates an advantage for Black.

## Presentation Slides
The slide deck summarizing the project, performance analysis, and algorithm details is located in the slides/ directory (file: Chess_AI_Slides.pdf).

## Contributing
Contributions, bug reports, and suggestions are welcome. Please open an issue or submit a pull request.

## License
© 2025 Aman Kumar. All rights reserved.
