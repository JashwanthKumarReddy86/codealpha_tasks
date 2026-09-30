import random

words = ["apple", "python", "school", "computer", "banana"]

word = random.choice(words)
guessed_letters = []
attempts = 6

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while attempts > 0:

    print(hangman[6 - attempts])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Remaining attempts:", attempts)

if attempts == 0:
    print(hangman[6])
    print("\nGame Over!")
    print("The word was:", word)

print("\nThank you for playing!")