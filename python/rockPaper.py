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
---'   ____)______
          ________)
          _________)
         _________)
---.___________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       ____________) 
      (______)
---.__(____)
'''

#Write your code below this line 👇
import random

group = [rock,paper,scissors]

user = int(input("what do you choose? type 0 for Rock, type 1 for Paper, type 2 for Scissors.\n"))

if 2 < user > 0 :
  print("wron number try angin")
else:
  print(group[user])
  print("computer choose:")
  com = random.randint(0,2)
  print(group[com])
  if user == 0 and com == 1:
    print("you lose")
  elif user == 0 and com == 2:
    print("you win")
  elif user == 1 and com == 0:
    print("you win")
  elif user == 1 and com == 2:
    print("you lose")
  elif user == 2 and com == 0:
    print("you lose")
  elif user == 2 and com == 1:
    print("you win")
  else:
    print("no one win")
