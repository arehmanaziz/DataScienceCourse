Hangman Game

This Hangman game is a simple interactive game implemented in Python. The game randomly selects a word from a predefined list, and the player attempts to guess the word by inputting letters. The game provides visual feedback using ASCII art to represent the current state of the player's progress and remaining lives.

## Instructions

1. **Choosing a Word:**
   - The game starts by randomly choosing a word from the `word_list` which includes words like "aardvark," "baboon," and "camel."
   - The chosen word is displayed to demonstrate the randomness of the selection.

2. **Display Initialization:**
   - An empty list named `display` is created to represent the current state of the guessed word.
   - Each letter in the chosen word is initially represented by an underscore ("_").
   - The user is prompted to guess a letter, and the program checks if the guessed letter is in the chosen word.

3. **Letter Guessing Loop:**
   - The game uses a while loop to allow the player to continue guessing until they have guessed all the letters in the chosen word.
   - In each iteration, the player is prompted to guess a letter.
   - The program reveals the correctly guessed letters in the display, and the player continues guessing until the entire word is revealed.

4. **ASCII Art and Lives:**
   - The game includes ASCII art representations for different stages of the hangman.
   - The player starts with 6 lives, and each incorrect guess results in a deduction of a life.
   - If the player exhausts all lives, the game ends, and "You lose!" is displayed.

5. **Handling Repeated and Incorrect Guesses:**
   - The game checks if the guessed letter has already been guessed and informs the player.
   - If the guessed letter is not in the chosen word, the game prints an "Incorrect guess" message, updates the ASCII art, and reduces the number of remaining lives.

## Conclusion
This Hangman game provides a fun and interactive way for users to guess words while enjoying visual feedback in the form of ASCII art. Players can continue guessing until they either successfully guess the entire word or run out of lives. Have fun playing the game!
