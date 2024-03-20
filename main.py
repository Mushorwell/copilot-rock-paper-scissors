import random
import time
import os

# create a rock, paper, scissors cli game using python
from termcolor import colored

ascii_art = {
        "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
        "lizard": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
        "spock": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    }

def clear_screen():
    # 'cls' for Windows, 'clear' for Linux and macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    print(colored("\nChoose your option:", 'cyan'))
    for i, choice in enumerate(choices, 1):
        print(colored(f"{i}. {choice.capitalize()}", 'green'))
    while True:
        try:
            user_choice = input(colored("\nEnter your choice (1-5, r, p, s, l, sp, rock, paper, scissors, lizard, spock): ", 'cyan')).lower()
            if user_choice in ["1", "2", "3", "4", "5"]:
                user_choice = choices[int(user_choice) - 1]
            elif user_choice in ["r", "p", "s", "l", "sp"]:
                user_choice = choices[["r", "p", "s", "l", "sp"].index(user_choice)]
            elif user_choice not in choices:
                raise ValueError("Invalid choice. Please try again.")
            print(ascii_art[user_choice])
            return user_choice
        except ValueError as e:
            print(colored(e, 'red'))

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)
    print(ascii_art[computer_choice])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    rules = {"rock": ["scissors", "lizard"], "paper": ["rock", "spock"], "scissors": ["paper", "lizard"], "lizard": ["spock", "paper"], "spock": ["scissors", "rock"]}
    if computer_choice in rules[user_choice]:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    # Call the function to clear the screen
    clear_screen()

    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("1. Rock crushes Scissors and Lizard.")
    print("2. Paper covers Rock and disproves Spock.")
    print("3. Scissors cuts Paper and decapitates Lizard.")
    print("4. Lizard eats Paper and poisons Spock.")
    print("5. Spock smashes Scissors and vaporizes Rock.")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score: You - {user_score}, Computer - {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again not in ["y", "yes"]:
            break
        delay = random.randint(1, 5)  # random delay between 1 and 5 seconds
        print(f"Next round starts in {delay} seconds...")
        time.sleep(delay)
    print(f"Final score: You - {user_score}, Computer - {computer_score}")

play_game()