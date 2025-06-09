import random
import winsound

# Define the hangman figure
HANGMAN_FIGURES = {
    0: ("   o  ",
        "  /|\\",
        "  / \\"),
    1: ("   o  ",
        "  /|\\",
        "  / \\"),
    2: ("   o  ",
        "  /|\\",
        "  /|\\"),
    3: ("   o  ",
        "  /|\\",
        "  /|\\"),
    4: ("   o  ",
        "  /|\\",
        "  /|\\"),
    5: ("   o  ",
        "  /|\\",
        "  /|\\"),
    6: ("   o  ",
        "  /|\\",
        "  /|\\")
}

# Function to display the hangman figure
def display_hangman(incorrect_guesses):
    print("=======")
    for line in HANGMAN_FIGURES[incorrect_guesses]:
        print(line)
    print("=======")

# Define the words for the game
WORDS = ("apple", "grape", "mango", "banana", "orange", "watermelon", "starfruit")

# Define the hangman figure for the game
GAME_HANGMAN_FIGURES = {
    0: (" _   ",
        "| \\   ",
        "|     ",
        "|     ",
        "|     "),
    1: (" _   ",
        "| \\   ",
        "|  o   ",
        "|     ",
        "|     "),
    2: (" _   ",
        "| \\   ",
        "|  o  ",
        "|  |  ",
        "|     "),
    3: (" _   ",
        "| \\   ",
        "|  o  ",
        "| /|  ",
        "|     "),
    4: (" _   ",
        "| \\   ",
        "|  o  ",
        "| /|\\",
        "|     "),
    5: (" _   ",
        "| \\   ",
        "|  o  ",
        "| /|\\",
        "| /   "),
    6: (" _   ",
        "| \\   ",
        "|  o  ",
        "| /|\\",
        "| / \\")
}

# Function to display the game hangman figure
def display_game_hangman(incorrect_guesses):
    print()
    print("=======")
    for line in GAME_HANGMAN_FIGURES[incorrect_guesses]:
        print(line)
    print("=======")

# Function to display the hint
def display_hint(hint):
    print(" ".join(hint))

# Function to display the answer
def display_answer(answer):
    print(" ".join(answer))

# Function for the Russian Roulette game
def russian_roulette():
    print("\n   ============Russian Roulette============")
    print("Note: You have a pistol with 6 slots. One of them has a bullet.")
    print("    - Pull the trigger several times. Good luck!")
    print()
    bullet_position = random.randint(1, 6)
    round_num = 0

    while True:
        round_num += 1
        input(f"Round {round_num}: Press Enter to pull the trigger...")
        chamber_position = random.randint(1, 6)

        print(f"The bullet is in slot {bullet_position}.")
        print(f"You pulled the trigger in slot {chamber_position}.")

        if chamber_position == bullet_position:
            print("BANG! YOU'RE DEAD")
            winsound.Beep(2500, 4000)
            display_hangman(0)
            break
        else:
            print("Click... you're safe!")
            choice = input("Do you want to play again? (y/n): ").lower()
            print()
            if choice != 'y':
                print("Thank you!")
                break

# Main function for the game
def main():
    answer = random.choice(WORDS)
    hint = ["_"] * len(answer)
    incorrect_guesses = 0
    guessed_letters = set()
    is_running = True

    print("Welcome to Hangman")
    while is_running:
        display_game_hangman(incorrect_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"You already guessed {guess}")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            incorrect_guesses += 1

        if "_" not in hint:
            display_game_hangman(incorrect_guesses)
            display_answer(answer)
            print("Congratulations, you won!")
            is_running = False
        elif incorrect_guesses >= len(GAME_HANGMAN_FIGURES) - 1:
            display_game_hangman(incorrect_guesses)
            display_answer(answer)
            print("You're dead!")
            winsound.Beep(2500, 3000)
            is_running = False

# Main loop
while True:
    print("Which game do you want to play?")
    print("1. Russian Roulette")
    print("2. Hangman")
    print("3. Exit")
    choice = input("(1/2/3): ")
    if choice == "1":
        russian_roulette()
    elif choice == "2":
        main()
    elif choice == "3":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")
        winsound.Beep(2500, 1500)
