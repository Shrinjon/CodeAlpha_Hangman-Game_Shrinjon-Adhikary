import random

# ASCII art for hangman stages
HANGMANPICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# List of possible words
words = ['python', 'java', 'developer', 'algorithm', 'hangman', 'programming', 'challenge', 'developer','apple','butterfly','rainbow','rhino','diamond','Lily','xylophone','watermellon','zebra','australia']

def get_random_word(word_list):
    """Choose a random word from the list of words."""
    word = random.choice(word_list)
    return word

def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    """Display the current board state."""
    print(HANGMANPICS[len(missed_letters)])
    print()

    print("Missed letters:", " ".join(missed_letters))

    blanks = ['_'] * len(secret_word)

    # Replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks[i] = secret_word[i]

    print(" ".join(blanks))
    print()

def get_guess(already_guessed):
    """Get the player's guess, ensuring it's a single valid letter."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

def play_again():
    """Ask the player if they want to play again."""
    return input("Do you want to play again? (yes or no): ").lower().startswith('y')

def play_hangman():
    print("H A N G M A N")
    
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_over = False

    while True:
        display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)

        # Get the player's guess
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            # Check if the player has won
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print(f"Yes! The secret word is \"{secret_word}\"! You have won!")
                game_over = True
        else:
            missed_letters += guess

            # Check if the player has guessed too many times and lost
            if len(missed_letters) == len(HANGMANPICS) - 1:
                display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was \"{secret_word}\".")
                game_over = True

        if game_over:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_over = False
                secret_word = get_random_word(words)
            else:
                break

# Start the game
play_hangman()
