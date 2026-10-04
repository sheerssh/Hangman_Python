import random
from words import word_list, Stages


lives = 5
chosen_word = random.choice(word_list)

# print(chosen_word)

placeholder = ""
for char in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False
correct_list = []
guessed_letters = []

while not game_over:

    user_guess = input("Guess the letter in the word: ").lower()

    if user_guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(user_guess)

    display = ""

    for letter in chosen_word:
        if letter == user_guess:
            display += letter

            if user_guess not in correct_list:
                correct_list.append(user_guess)

        elif letter in correct_list:
            display += letter

        else:
            display += "_"

    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    print(Stages[5 - lives])

    if lives == 0:
        game_over = True
        print(f"You lose! The word was {chosen_word}")

    elif "_" not in display:
        game_over = True
        print("You win!")