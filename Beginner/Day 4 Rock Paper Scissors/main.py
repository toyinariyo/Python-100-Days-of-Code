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
rps_art = [rock, paper, scissors] #rock is 0 showing rock art, paper is 1 showing  and scissors is 2
player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors \n"))
print(rps_art[player_choice]) #
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(rps_art[computer_choice])
if player_choice >= 3 or player_choice < 0:
    print("Invalid choice. You lose.")
elif player_choice == 0 and computer_choice == 2: #Player chooses rock and computer chooses scissors
    print("Rock beats scissors. You win!")
elif computer_choice > player_choice:
    print("You lose!")
elif computer_choice < player_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw!")
