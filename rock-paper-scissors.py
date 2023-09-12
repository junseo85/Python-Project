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

#Write your code below this line 👇
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if int(user_choice) == 0:
  print(rock)
elif int(user_choice) == 1:
  print(paper)
elif int(user_choice)== 2:
  print(scissors)

computer = random.randint(0,2)
print("Computer chose:")
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if int(user_choice) ==0:
  if computer == 2:
    print("You win")
  elif computer == 0:
    print("draw")
  else:
    print("You lose")
elif int(user_choice) ==1:
  if computer == 0:
    print("You win")
  elif computer == 1:
    print("draw")
  else:
    print("You lose")
elif int(user_choice) ==2:
  if computer == 1:
    print("You win")
  elif computer == 2:
    print("draw")
  else:
    print("You lose")