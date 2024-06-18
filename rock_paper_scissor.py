import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

is_game = True

while is_game:

    game_image = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_image[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")

    elif user_choice == 0 and computer_choice == 2:
        print("You win!")

    elif computer_choice == 0 and user_choice == 2:
        print("You Loss!")

    elif user_choice > computer_choice:
        print("You win!")

    elif computer_choice > user_choice:
        print("You lose!")

    elif computer_choice == user_choice:
        print("The game is draw!")

    is_game = input("Do you want to play again? Type 'yes' or 'no'.\n")
    if is_game == "no":
        is_game = False
        print("See you next time!")
