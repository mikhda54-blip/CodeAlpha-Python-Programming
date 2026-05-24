import random

words = ["apple", "tiger", "house", "green", "chair"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong = 6

guessed_letters = []

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    letter = input("Enter a letter: ").lower()

    if letter in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(letter)

    if letter in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter

    else:
        print("Wrong!")
        wrong_guesses += 1

if "_" not in guessed_word:
    print("\nYou Won!")
else:
    print("\nYou Lost!")

print("The word was:", word)
