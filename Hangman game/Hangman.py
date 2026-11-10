
import random

words = ["python", "developer", "programming", "computer", "database"]

secret_word = random.choice(words)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while wrong_attempts < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts left:", max_attempts - wrong_attempts)
    print("Guessed letters:", guessed_letters)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You have used all your attempts.")

if wrong_attempts == max_attempts:
    print("The correct word was:", secret_word)
