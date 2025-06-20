import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "developer"]

# Randomly choose a word from the list
word_to_guess = random.choice(word_list)
guessed_letters = []
attempts = 6  # Number of allowed incorrect guesses

# Display the hidden word
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])

# Main game loop
print("Welcome to Hangman!")

while attempts > 0:
    print("\nWord to guess:", display_word())
    print("Remaining attempts:",attempts)
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct!")
    else:
        print("Wrong guess.")
        attempts -= 1

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\nCongratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\nGame Over! The word was:", word_to_guess)
