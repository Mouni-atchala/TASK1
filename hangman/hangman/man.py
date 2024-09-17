import random

# Predefined list of words
words = ['python', 'hangman', 'challenge', 'programming', 'algorithm', 'random', 'developer']

def choose_word():
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    
           |   
           |   
           |
        --------
        """
    ]
    return stages[tries]

def play():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = set()
    tries = 6

    print("Welcome to Hangman!")
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"Current word: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            incorrect_guesses.add(guess)
            tries -= 1
            print(f"Incorrect guess. You have {tries} tries left.")
        
        print("\n" + "-"*20 + "\n")

    if tries == 0:
        print(display_hangman(tries))
        print(f"Sorry, you lost! The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}'.")

if __name__ == "__main__":
    play()
