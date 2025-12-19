Hangman Game (Python)

A simple and interactive command-line Hangman game developed using Python.  
The player selects a category and guesses letters to reveal a hidden word within a limited number of attempts.

This project demonstrates core Python concepts such as dictionaries, lists, sets, loops, and input validation.

>> Features
- Multiple word categories:
  - Food
  - Animals
  - Birds
  - Programming Languages
- Random word selection for every game
- Automatic handling of **multi-word answers** (spaces are revealed)
- Input validation (only single alphabet characters allowed)
- Tracks guessed letters
- Limited attempts
- Clear win and game-over conditions

>> Technologies Used
- **Python 3**
- Built-in **random** module

>> How the Game Works
1. The user selects a category.
2. A random word is chosen from the selected category.
3. Letters are hidden using underscores (`_`).
4. Spaces in multi-word answers are displayed automatically.
5. The player guesses one letter at a time.
6. Correct guesses reveal letters in the word.
7. Incorrect guesses reduce the number of remaining attempts.
8. The game ends when:
   - All letters are revealed (**Win**), or
   - The player runs out of attempts (**Game Over**).

 >> How to Run the Game
1. Make sure Python 3 is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python hangman.py
