# Python Quiz Program
## Geography Quiz
A console-based Python quiz program that tests your geography knowledge, tracks scores, and maintains a persistent high score across sessions.

Built as part of my Python learning journey, focused on file handling, data persistence, and program logic.

## Features
- Randomised questions: different order every time you play
- High score tracking: persists across sessions using CSV storage
- Scoreboard: view all previous scores before playing
- Input validation: handles invalid entries gracefully
- CSV-based storage: questions and scores managed through plain CSV files

## Project Structure
geography-quiz/

├── main.py              # Main program

├── questions1.csv       # Quiz questions (question, options, answer)

├── quiz_scores.csv      # Scoreboard — auto-created on first run

├── high_score.csv       # High score record — auto-created on first run

└── README.md

## Requirements
- Python 3.x
- No external libraries required — uses Python's built-in csv, random, and os modules
- **Run the quiz:** python main.py
## Example Output
===== Geography Quiz =====

View scoreboard before playing? (Y/N): Y

===== Scoreboard =====

Player Name: Total Score

Aleena: 10
  
  Albi: 11

=======================

Enter your name: Alice

Which is the smallest country in the world?
A. Andorra  B. Luxembourg  C. Belgium  D. Vatican City

Type A, B, C, or D: D
Correct answer!

What is the tallest waterfall in the world?
A. Niagara Falls  B. Angel Falls  C. Victoria Falls  D. Tugela Falls

Type A, B, C, or D: B
Correct answer!

...

Alice, your Total Score: 11/12.
Your score has been saved, Alice!
You tied the high score of 11 held by Albi!

Thanks for playing! Goodbye!

## What I Learned
- Reading and writing CSV files using Python's csv module
- Persistent data storage across program sessions
- Randomising data with the random module
- Input validation and loop control
- Structuring a program using functions for readability

## Future Improvements
- [ ] Add difficulty levels (easy / medium / hard)
- [ ] Support multiple quiz topics beyond geography
