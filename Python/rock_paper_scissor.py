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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissor")
user_choice = input("Enter  Rock, Paper or Scissor: ").lower()


choices = ['rock','paper','scissor']



computer_choice = random.choice(choices)

print(f"You chose {user_choice}")
if user_choice == 'rock':
  print(rock)
elif user_choice == 'paper':
  print(paper)
else :
  print(scissor)

print(f"Computer chose {computer_choice}")
if computer_choice == 'rock':
  print(rock)
elif computer_choice == 'paper':
  print(paper)
else :
  print(scissor)

if computer_choice == 'rock' and user_choice == 'scissor':
  print("Computer Wins!")
elif computer_choice == 'paper' and user_choice == 'rock':
  print("Computer Wins!")
elif computer_choice == 'scissor' and user_choice == 'paper':
  print("Computer Wins!")
elif computer_choice == 'rock' and user_choice == 'paper':
  print("You win")
elif computer_choice == 'paper' and user_choice == 'scissor':
  print("You win")
elif computer_choice == 'scissor' and user_choice == 'rock':
  print("You win")
else:
  print("Draw!")