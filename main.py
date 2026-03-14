import csv
import random
import os

# Initialize variables
score = 0
question_no = 0
options = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Function to check the guess
def check_guess(guess, answer):
    global score, question_no
    if guess == answer:
        print('Correct answer!')
        score += 1
    else:
        print(f'Wrong! The correct answer is: {answer}')
    question_no += 1

# Function to show the total score
def show_score(name):
    print(f"\n{name}, your Total Score: {score}/{question_no}.")
    save_score(name, score)
    check_high_score(name, score)

# Function to save the user's score to a CSV file
def save_score(name, score):
    file_exists = os.path.isfile('quiz_scores.csv')
    with open('quiz_scores.csv', mode='a', newline='') as score_file:
        score_writer = csv.writer(score_file)
        # Only write the header if the file is new
        if not file_exists:
            score_writer.writerow(['Player Name', 'Total Score'])
        score_writer.writerow([name, score])
    print(f"Your score has been saved, {name}!")

# Function to check and display the high score
def check_high_score(name, current_score):
    high_score, high_scorer = read_high_score()

    if current_score > high_score:
        print(f"Congratulations {name}! You've beaten the high score with {current_score}!")
        save_high_score(name, current_score)
    elif current_score == high_score:
        print(f"You tied the high score of {high_score} held by {high_scorer}!")
    else:
        print(f"The current high score is {high_score} by {high_scorer}. Can you beat it?")

# Function to save the high score and name to a CSV file
def save_high_score(name, score):
    with open('high_score.csv', mode='w', newline='') as high_score_file:
        score_writer = csv.writer(high_score_file)
        score_writer.writerow([name, score])

# Function to read the high score from a CSV file
def read_high_score():
    try:
        with open('high_score.csv', mode='r') as high_score_file:
            score_reader = csv.reader(high_score_file)
            for row in score_reader:
                return int(row[1]), row[0]  # score, name
    except (FileNotFoundError, IndexError):
        return 0, "No one yet"# If no high score file exists, return 0 as the default high score

# Function to display the scoreboard
def show_scoreboard():
    print("\n===== Scoreboard =====")
    try:
        with open('quiz_scores.csv', mode='r') as score_file:
            score_reader = csv.reader(score_file)
            rows = list(score_reader)
            if len(rows) <= 1:
                print("No scores yet!")
            else:
                for row in rows:
                    print(f"  {row[0]}: {row[1]}")
    except FileNotFoundError:
        print("No scores recorded yet.")
    print("======================\n")

# Main quiz function
if __name__ == "__main__":
    print('===== Geography Quiz =====')

    # Ask if they want to see the scoreboard first
    view_board = input("View scoreboard before playing? (Y/N): ").upper()
    if view_board == 'Y':
        show_scoreboard()

    # Get the player's name
    player_name = input("Enter your name: ")

    with open('questions1.csv', 'r') as csvfile:
        csvreader = list(csv.reader(csvfile))
        header = csvreader[0]  # Skip the header
        questions = csvreader[1:]  # All rows after the header

        # Randomize questions
        random.shuffle(questions)

        for row in questions:
            print(f"\n{row[0]}\nA. {row[1]}  B. {row[2]}  C. {row[3]}  D. {row[4]}\n")
            correct_choice = False

            while not correct_choice:
                guess = input("Type A, B, C, or D: ").upper()
                if guess in ['A', 'B', 'C', 'D']:
                    check_guess(row[options[guess]], row[5])
                    correct_choice = True
                else:
                    print("Invalid input. Please type A, B, C, or D.")

        # Show the final score after all questions
        show_score(player_name)

    print('\nThanks for playing! Goodbye!')