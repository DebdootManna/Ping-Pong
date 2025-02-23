# Ping Pong Game in Python

This is a classic Ping Pong game built using Python and Pygame. The game supports both a two-player mode and a single-player mode where you play against an AI-controlled bot. The gameplay includes real-time score tracking, sound effects, and increasing ball speed over time.

## Features

- **Game Modes:**
  - 2-Player mode (Player 1: `W` and `S`, Player 2: `UP` and `DOWN`)
  - Play against an AI bot
- **Smooth and responsive paddle movement**
- **Ball speed increases over time**
- **Live score display**
- **Sound effects for ball bounce and scoring**
- **Minimalistic and visually appealing UI**

## Installation

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies
To install the required dependencies, run:

```bash
pip install pygame pandas numpy
```

## How to Play

1. **Run the game**
   ```bash
   python pingpong.py
   ```
2. **Select the game mode:**
   - Press `1` for a 2-player game.
   - Press `2` to play against the bot.
3. **Control your paddle:**
   - **Player 1:** `W` (up) and `S` (down)
   - **Player 2 / AI Opponent:** `UP` (up) and `DOWN` (down)
4. **Score points by making the opponent miss the ball!**

## File Structure
```
Ping Pong Game/
│── pingpong.py         # Main game file
│── score.csv           # Stores player scores
│── bounce.wav          # Sound effect for ball bounce
│── score.wav           # Sound effect for scoring
│── README.md           # Project documentation
```

## Future Improvements
- Add difficulty levels for AI
- Implement a pause and restart feature
- Improve AI movement to make it more challenging

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this repository, improve the game, and submit a pull request!

---

Enjoy the game and have fun! 🏓

